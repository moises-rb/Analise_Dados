# 📏 Fase Measure - Distribuição Estatística

Este notebook corresponde à fase **Measure** do projeto Green Belt, com foco em avaliar a **distribuição estatística da variável crítica `Tempo_atendimento`**, que impacta diretamente na percepção de qualidade do serviço prestado.

---

## 🎯 Objetivo

Compreender a distribuição dos dados e testar sua aderência à normalidade é essencial para aplicar ferramentas estatísticas apropriadas nas próximas fases do DMAIC. Essa etapa responde:

- Os dados seguem distribuição normal?
- Existem outliers ou assimetrias?
- Qual é o grau de variabilidade do processo?

---

## 🔍 Análises Realizadas

- 📊 Histograma e boxplot da variável `Tempo_atendimento`
- 📈 QQ-Plot para análise visual da normalidade
- 🧪 Teste de Shapiro-Wilk
- 🧪 Teste de Anderson-Darling (via Minitab)
- 📉 Estatísticas descritivas:
  - Média
  - Mediana
  - Desvio padrão
  - Curtose
  - Assimetria (Skewness)

---

## 📌 Principais Resultados

- A distribuição dos dados apresenta **assimetria à direita** e presença de outliers.
- Os testes de normalidade retornaram **p-valores < 0.05**, rejeitando a hipótese de normalidade.
- O QQ-Plot reforçou visualmente o desvio da normalidade.
- A análise indica que o processo não segue uma distribuição normal, sendo necessário considerar **testes não paramétricos** nas etapas seguintes.

---

## 🧰 Ferramentas e Bibliotecas Utilizadas

- **Python**: 
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scipy.stats`
  - `statsmodels`
- **Minitab**: para reforço visual e validação cruzada dos testes de normalidade
- **Jupyter Notebook**: como ferramenta de análise e documentação

---

## 📂 Estrutura da Pasta

```bash
📦 DistribuicaoEstatistica
 ┣ 📁 images
 ┃ ┣ 📄 histograma.png
 ┃ ┣ 📄 boxplot.png
 ┃ ┗ 📄 qqplot.png
 ┣ 📄 DistribuicaoEstatistica.ipynb
 ┗ 📄 README.md
```
---

## ✅ Conclusão

A etapa de "Measure" cumpriu seu papel de fornecer **entendimento estatístico detalhado** do comportamento da variável `Tempo_atendimento`. Confirmamos que os dados **não seguem distribuição normal** e possuem **variabilidade significativa**, o que orientará a escolha dos métodos analíticos mais apropriados na fase **Analyse**.

---

## 👨‍💼 Autor

**Moisés Ribeiro**  
Projeto Green Belt - Análise de Dados e Melhoria de Processos  
[🔗 LinkedIn](https://www.linkedin.com/in/moisesrsjr/)  
[💻 Repositório Principal](https://github.com/moises-rb)

---

## 📝 Observações

Este projeto é parte da minha formação em **Melhoria Contínua** com foco na certificação **Green Belt Seis Sigma**.  
Todos os dados foram tratados e, quando necessário, **anonimizados** com fins **educacionais e acadêmicos**.
