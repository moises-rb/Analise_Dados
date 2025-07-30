# scripts/data_loader.py

import pandas as pd
import requests
import os
from io import StringIO
import logging

# Configurar logging para mensagens de carregamento (melhor que print para funções)
# Você pode ajustar o nível (INFO, WARNING, ERROR) conforme preferir
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_data_with_fallback(
    github_raw_url: str,
    file_name: str = 'df_final.csv',
    local_data_dir: str = 'dados',
    timeout_seconds: int = 100
) -> pd.DataFrame:
    """
    Tenta carregar um DataFrame de uma URL raw do GitHub.
    Em caso de falha (timeout, erro de conexão, etc.), tenta carregar
    o DataFrame de uma cópia local no diretório do projeto.

    Args:
        github_raw_url (str): A URL completa do arquivo raw no GitHub.
        file_name (str): O nome do arquivo CSV (ex: 'df_final.csv').
                         Usado para o caminho local.
        local_data_dir (str): O nome da pasta onde os dados locais estão (ex: 'dados').
                              Assumido estar no mesmo nível da 'Pasta do Projeto'.
        timeout_seconds (int): Tempo limite em segundos para a requisição HTTP do GitHub.

    Returns:
        pd.DataFrame: O DataFrame carregado, ou None se não for possível carregar de nenhuma fonte.
    """
    dados = None
    
    # Obter o diretório base do projeto de forma robusta
    # Isso assume que o script `data_loader.py` estará dentro da pasta 'scripts'
    # e que 'scripts' está no mesmo nível de 'dados' e 'notebooks'.
    # O dirname(dirname(__file__)) irá do 'data_loader.py' -> 'scripts' -> 'Pasta do Projeto'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_data_path = os.path.join(base_dir, local_data_dir, file_name)

    logging.info(f"Tentando ler os dados do GitHub da URL: {github_raw_url}")
    try:
        response = requests.get(github_raw_url, timeout=timeout_seconds)
        response.raise_for_status() # Lança um erro para status codes 4xx/5xx

        dados = pd.read_csv(StringIO(response.text))
        logging.info("Dados lidos com sucesso do GitHub!")

    except requests.exceptions.Timeout:
        logging.warning("Tempo limite de conexão excedido ao tentar ler do GitHub.")
        logging.info(f"Tentando ler da cópia local em: {local_data_path}")
    except requests.exceptions.ConnectionError:
        logging.warning("Erro de conexão ao tentar ler do GitHub. Verifique sua internet ou a URL.")
        logging.info(f"Tentando ler da cópia local em: {local_data_path}")
    except requests.exceptions.RequestException as e:
        logging.warning(f"Erro de requisição inesperado ao tentar ler do GitHub: {e}")
        logging.info(f"Tentando ler da cópia local em: {local_data_path}")
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado ao tentar ler do GitHub: {e}")
        logging.info(f"Tentando ler da cópia local em: {local_data_path}")

    # Se o DataFrame ainda não foi carregado (houve um erro ao ler do GitHub)
    if dados is None:
        try:
            if os.path.exists(local_data_path):
                dados = pd.read_csv(local_data_path)
                logging.info("Dados lidos com sucesso da cópia local!")
            else:
                logging.error(f"Erro: O arquivo '{local_data_path}' não foi encontrado na pasta '{local_data_dir}'.")
                logging.warning("Por favor, certifique-se de que o arquivo esteja lá e que o nome esteja correto.")
        except Exception as e:
            logging.error(f"Erro inesperado ao tentar ler da cópia local: {e}")

    if dados is not None:
        logging.info(f"DataFrame carregado com sucesso! Shape: {dados.shape}")
        return dados
    else:
        logging.error("Não foi possível carregar o DataFrame de nenhuma fonte.")
        logging.warning("Por favor, verifique a URL do GitHub, sua conexão e o caminho/existência do arquivo local.")
        return None # Retorna None se o carregamento falhar completamente