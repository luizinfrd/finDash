import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Organizador Financeiro", layout="wide")

# --- FUNÇÕES AUXILIARES (A Lógica) ---

def categorizar_despesa(descricao: str) -> str:
    """
    Analisa a descrição da transação e retorna uma categoria correspondente.
    """
    if not isinstance(descricao, str):
        return 'Outros'
        
    descricao = descricao.upper()
    
    # Dicionário de regras poderia ser implementado aqui no futuro
    if 'IFOOD' in descricao or 'RESTAURANTE' in descricao or 'PADARIA' in descricao:
        return 'Alimentação'
    elif 'UBER' in descricao or '99POP' in descricao:
        return 'Transporte'
    elif 'NETFLIX' in descricao or 'SPOTIFY' in descricao or 'AMAZON' in descricao:
        return 'Assinaturas e Lazer'
    elif 'SUPERMERCADO' in descricao or 'MERCADO' in descricao:
        return 'Mercado'
    elif 'FARMACIA' in descricao or 'SAUDE' in descricao:
        return 'Saúde'
    else:
        return 'Outros'

def processar_dados(df: pd.DataFrame):
    """
    Aplica a categorização e separa receitas de despesas.
    """
    df['Categoria'] = df['Descricao'].apply(categorizar_despesa)
    
    # Separação de dados
    df_despesas = df[df['Valor'] < 0].copy()
    df_receitas = df[df['Valor'] > 0].copy()
    
    # Converte despesas para positivo para facilitar a visualização
    df_despesas['Valor'] = df_despesas['Valor'].abs()
    
    return df_receitas, df_despesas

# --- APLICAÇÃO PRINCIPAL (A Interface) ---

def main():
    st.title("Seja bem vindo ao FinDash, o seu organizador de Finanças Pessoais 💰")
    st.markdown("Faça o upload do seu extrato e tenha uma visão clara das suas finanças.")

    # 1. Upload do Arquivo
    arquivo_upload = st.file_uploader("Selecione seu arquivo CSV", type="csv")

    if arquivo_upload is not None:
        try:
            # Leitura dos dados
            df_bruto = pd.read_csv(arquivo_upload)
            
            # Converter coluna Data para datetime (Essencial para o filtro funcionar)
            df_bruto['Data'] = pd.to_datetime(df_bruto['Data'], dayfirst=True, errors='coerce')
            
            # Filtro de Data na Sidebar
            st.sidebar.header("Filtros")
            if not df_bruto['Data'].isnull().all():
                min_date = df_bruto['Data'].min()
                max_date = df_bruto['Data'].max()
                
                periodo = st.sidebar.date_input(
                    "Selecione o Período",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date
                )
                
                if len(periodo) == 2:
                    df_bruto = df_bruto[
                        (df_bruto['Data'].dt.date >= periodo[0]) & #dt é uma palavra reservada do pandas.
                        (df_bruto['Data'].dt.date <= periodo[1])
                    ]
            
            # Exibição prévia (opcional, dentro de um expander para limpar a tela)
            with st.expander("🔍 Visualizar dados brutos"):
                st.dataframe(df_bruto.head())

            # 2. Processamento
            df_receitas, df_despesas = processar_dados(df_bruto)

            # 3. Dashboard (Métricas)
            st.divider()
            col1, col2, col3 = st.columns(3)
            
            total_receita = df_receitas['Valor'].sum()
            total_despesa = df_despesas['Valor'].sum()
            saldo = total_receita - total_despesa

            col1.metric("Receitas", f"R$ {total_receita:,.2f}")
            col2.metric("Despesas", f"R$ {total_despesa:,.2f}")
            col3.metric("Saldo", f"R$ {saldo:,.2f}", delta_color="normal")

            # 4. Visualização (Gráfico)
            st.divider()
            st.subheader("📊 Para onde foi o dinheiro?")
            
            if not df_despesas.empty:
                fig, ax = plt.subplots(figsize=(10, 5))
                gastos_por_categoria = df_despesas.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
                
                gastos_por_categoria.plot(kind='bar', ax=ax, color='#4CAF50', edgecolor='black')
                
                ax.set_ylabel('Valor (R$)')
                ax.set_xlabel('')
                plt.xticks(rotation=45, ha='right')
                plt.grid(axis='y', linestyle='--', alpha=0.3)
                plt.tight_layout() # Ajuste fino para não cortar textos
                
                st.pyplot(fig)
            else:
                st.info("Nenhuma despesa encontrada para gerar o gráfico.")

        except Exception as e:
            st.error(f"Ops! Ocorreu um erro ao processar o arquivo: {e}")

if __name__ == "__main__":

    main()
