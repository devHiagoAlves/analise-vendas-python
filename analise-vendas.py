import pandas as pd

url = "https://raw.githubusercontent.com/devHiagoAlves/analise-vendas-python/main/vendas.csv"
dados = pd.read_csv(url)
print(dados)
