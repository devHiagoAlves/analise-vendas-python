import pandas as pd
import matplotlib.pyplot as plt

# Lendo direto do GitHub
url = "https://raw.githubusercontent.com/devHiagoAlves/analise-vendas-python/main/vendas.csv"
dados = pd.read_csv(url)

# Criando a coluna de valor total
dados["Valor_total"] = dados["Quantidade"] * dados["Preco_unitario"]

# Gráfico de barras
dados.groupby("Vendedor")["Valor_total"].sum().plot(kind="bar", color="skyblue")
plt.title("Total vendido por vendedor")
plt.ylabel("Valor em R$")
plt.xlabel("Vendedor")
plt.show()

dados.groupby("Produto")["Quantidade"].sum().plot(kind="pie", autopct="%1.1f%%") 
plt.title("Participação de cada produto nas vendas") 
plt.ylabel("") # remove o rótulo lateral plt.show()
