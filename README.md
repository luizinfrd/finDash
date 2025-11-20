# 💰 FinDash - Organizador Financeiro Pessoal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Status-MVP-orange)

> Transforme extratos bancários confusos em dashboards visuais e insights claros em segundos.

---

## 📸 Demonstração

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/83070b92-4f7e-4f92-b574-b6285971d01d" />


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
    git clone https://github.com/luizinfrd/finDash.git
    cd finDash
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

6.  **Padronização dos arquivos**
    Você pode selecionar seu arquivo, mas verifique se ele está no padrão recomendado.
    Utilize o arquivo "extratoExemplo.csv" para entender o padrão aceito ou utilize o
    arquivo "extrato_anual.csv" para um exemplo robusto do dashboard.


## 🔮 Próximos Passos (Roadmap)

* [ ] Adicionar filtro por data (mês/ano).
* [ ] Permitir que o usuário edite categorias manualmente na tela.
* [ ] Exportar o relatório final em PDF ou Excel.
