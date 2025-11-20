import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações
NUM_TRANSACOES = 500
DATA_INICIAL = datetime(2025, 1, 1)

# Listas de possibilidades para criar dados aleatórios
descricoes_despesas = [
    ('UBER VIAGENS', -15, -50),
    ('IFOOD PEDIDO', -30, -120),
    ('MERCADO COMPRA', -100, -800),
    ('NETFLIX ASSINATURA', -39.90, -55.90),
    ('SPOTIFY PREMIUM', -21.90, -21.90),
    ('AMAZON COMPRA', -50, -500),
    ('PADARIA DO BÁIRRO', -10, -40),
    ('FARMACIA SAUDE', -20, -200),
    ('POSTO DE GASOLINA', -100, -300),
    ('CINEMA INGRESSO', -30, -80)
]

receitas = [
    ('SALARIO MENSAL', 3500, 5000),
    ('FREELA PROJETO PYTHON', 500, 1500),
    ('REEMBOLSO FIRMA', 100, 400)
]

dados = []

# Gera as transações
for _ in range(NUM_TRANSACOES):
    # 90% de chance de ser despesa, 10% de ser receita
    if random.random() < 0.9:
        desc, min_val, max_val = random.choice(descricoes_despesas)
    else:
        desc, min_val, max_val = random.choice(receitas)
    
    # Gera valor e data aleatória
    valor = round(random.uniform(min_val, max_val), 2)
    dias_aleatorios = random.randint(0, 365)
    data = DATA_INICIAL + timedelta(days=dias_aleatorios)
    
    dados.append([data.strftime('%Y-%m-%d'), desc, valor])

# Cria o DataFrame e salva
df = pd.DataFrame(dados, columns=['Data', 'Descricao', 'Valor'])
df = df.sort_values(by='Data') # Ordena por data para ficar bonito

nome_arquivo = 'extrato_anual.csv'
df.to_csv(nome_arquivo, index=False)

print(f"Sucesso! Arquivo '{nome_arquivo}' gerado com {NUM_TRANSACOES} linhas.")