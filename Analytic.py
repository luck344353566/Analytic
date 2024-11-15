# Programa de Treinamento em Dados para Mercearia e Panificação Tawany

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import random

# Módulo 1: Coleta de Dados
# --------------------------
# Este módulo simula a coleta de dados de vendas, inventário e feedback dos clientes.
# Em um ambiente real, esses dados seriam importados de sistemas de ponto de venda ou planilhas de inventário.

def gerar_dados_vendas():
    produtos = ["Pão", "Leite", "Queijo", "Café", "Bolo", "Biscoito"]
    dados_vendas = {
        "Produto": [random.choice(produtos) for _ in range(100)],
        "Quantidade": [random.randint(1, 20) for _ in range(100)],
        "Data": [datetime(2023, random.randint(1, 12), random.randint(1, 28)) for _ in range(100)],
        "Valor Unitário": [round(random.uniform(2, 20), 2) for _ in range(100)],
    }
    vendas_df = pd.DataFrame(dados_vendas)
    vendas_df["Valor Total"] = vendas_df["Quantidade"] * vendas_df["Valor Unitário"]
    return vendas_df

# Exemplo de execução:
vendas_df = gerar_dados_vendas()
print("Dados de vendas coletados:\n", vendas_df.head())

# Módulo 2: Análise de Dados
# --------------------------
# Este módulo realiza uma análise básica dos dados de vendas, como total de vendas por produto e receita diária.

def analise_basica(vendas_df):
    # Total de vendas por produto
    vendas_por_produto = vendas_df.groupby("Produto")["Valor Total"].sum()
    print("\nVendas totais por produto:")
    print(vendas_por_produto)

    # Receita diária
    receita_diaria = vendas_df.groupby("Data")["Valor Total"].sum()
    print("\nReceita diária:")
    print(receita_diaria)

    # Gráfico de vendas por produto
    vendas_por_produto.plot(kind="bar", title="Vendas Totais por Produto")
    plt.ylabel("Receita Total (R$)")
    plt.show()

    # Gráfico de receita diária
    receita_diaria.plot(kind="line", title="Receita Diária")
    plt.ylabel("Receita (R$)")
    plt.xlabel("Data")
    plt.xticks(rotation=45)
    plt.show()

# Exemplo de execução:
analise_basica(vendas_df)

# Módulo 3: Interpretação de Dados
# -------------------------------
# Este módulo ajuda a identificar produtos mais vendidos, sazonalidade e preferência dos clientes.
# Os resultados podem ser usados para ajustar inventário e promoções.

def interpretacao_dados(vendas_df):
    # Produtos mais vendidos
    produtos_mais_vendidos = vendas_df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)
    print("\nProdutos mais vendidos (em quantidade):")
    print(produtos_mais_vendidos)

    # Análise sazonal (exemplo para identificar padrões de vendas por mês)
    vendas_df["Mes"] = vendas_df["Data"].dt.month
    vendas_por_mes = vendas_df.groupby("Mes")["Valor Total"].sum()
    
    # Gráfico de vendas por mês
    vendas_por_mes.plot(kind="bar", title="Vendas Totais por Mês")
    plt.ylabel("Receita Total (R$)")
    plt.xlabel("Mês")
    plt.xticks(rotation=0)
    plt.show()

    # Análise de preço médio por produto
    preco_medio_produto = vendas_df.groupby("Produto")["Valor Unitário"].mean()
    print("\nPreço médio por produto:")
    print(preco_medio_produto)

# Exemplo de execução:
interpretacao_dados(vendas_df)

# Módulo 4: Relatórios e Insights
# ------------------------------
# Este módulo gera relatórios e fornece insights para ajudar na tomada de decisões.

def gerar_relatorio(vendas_df):
    print("\n==== Relatório de Vendas ====")
    total_receita = vendas_df["Valor Total"].sum()
    produtos_mais_vendidos = vendas_df.groupby("Produto")["Quantidade"].sum().idxmax()
    produto_maior_receita = vendas_df.groupby("Produto")["Valor Total"].sum().idxmax()
    
    print(f"Receita total: R$ {total_receita:.2f}")
    print(f"Produto mais vendido (quantidade): {produtos_mais_vendidos}")
    print(f"Produto com maior receita: {produto_maior_receita}")

# Exemplo de execução:
gerar_relatorio(vendas_df)
