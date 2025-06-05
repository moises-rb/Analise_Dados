
# paleta_cores.py
# Paleta de cores personalizada - Moisés Ribeiro

import matplotlib.pyplot as plt

# Dicionário com as cores da paleta
telecom_palette = {
    'azul_principal': '#004E89',
    'azul_secundario': '#1A659E',
    'ciano': '#3EA8A1',
    'verde': '#3FA34D',
    'amarelo': '#FFB30F',
    'laranja': '#F35B04',
    'vermelho': '#D7263D',
    'roxo': '#6A0572',
    'cinza_escuro': '#3C3C3C',
    'cinza_claro': '#BFBFBF'
}

def get_telecom_color(nome_cor):
    """Retorna o código hexadecimal da cor."""
    return telecom_palette.get(nome_cor, None)

def show_colors():
    """Exibe a paleta de cores."""
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_xlim(0, len(telecom_palette))
    ax.set_ylim(0, 1)
    ax.axis('off')

    for i, (nome, cor) in enumerate(telecom_palette.items()):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=cor))
        ax.text(i + 0.5, -0.1, nome, ha='center', va='top', fontsize=8, rotation=45)

    plt.show()
