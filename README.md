# 💰 FinDash - Organizador Financeiro Pessoal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Status-MVP-orange)

> Transforme extratos bancários confusos em dashboards visuais e insights claros em segundos.

---

## 📸 Demonstração

![Screenshot do Projeto]([INSIRA_AQUI_O_LINK_DA_IMAGEM_OU_CAMINHO_LOCAL])
*(Substitua isso por um print da tela do seu projeto rodando!)*

## 🎯 Sobre o Projeto

O **FinDash** nasceu de uma necessidade real: a dificuldade de categorizar e visualizar gastos pessoais a partir de extratos bancários brutos (CSV). 

Muitas pessoas perdem horas planilhando gastos manualmente. Este projeto automatiza esse processo, lendo arquivos CSV, aplicando regras inteligentes de categorização e gerando gráficos intuitivos para análise financeira.

### ✨ Funcionalidades Principais
* **Upload de Arquivos:** Interface simples para carregar extratos em CSV.
* **Categorização Automática:** Lógica inteligente que identifica despesas baseada na descrição (Ex: Uber -> Transporte).
* **Dashboard Interativo:** Métricas claras de Receita, Despesa e Saldo.
* **Visualização de Dados:** Gráficos de barras gerados automaticamente para identificar os maiores gastos.
* **Privacidade:** O processamento é feito localmente ou em sessão temporária, garantindo segurança dos dados.

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem base do projeto.
* **[Streamlit](https://streamlit.io/):** Para criação da interface web interativa.
* **[Pandas](https://pandas.pydata.org/):** Para manipulação e análise tabular dos dados.
* **[Matplotlib](https://matplotlib.org/):** Para geração dos gráficos.

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para rodar o FinDash na sua máquina local:

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO]/[NOME_DO_REPOSITORIO].git
    cd [NOME_DO_REPOSITORIO]
    ```

2.  **Crie um ambiente virtual (Recomendado)**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação**
    ```bash
    streamlit run main.py
    ```

5.  **Acesse no navegador**
    O Streamlit abrirá automaticamente o link (geralmente `http://localhost:8501`).

---
