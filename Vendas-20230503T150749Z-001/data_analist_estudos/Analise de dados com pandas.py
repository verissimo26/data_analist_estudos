#import
import os
import pandas as pd

lista_arquivos = os.listdir("/content/drive/MyDrive/curso_basico_python/Vendas")
display (lista_arquivos)

# ------------

tabela_total = pd.DataFrame()
for arquivo in lista_arquivos: 
  if "Vendas" in arquivo:
   tabela = pd.read_csv(f"/content/drive/MyDrive/curso_basico_python/Vendas/{arquivo}")
   tabela_total = tabela_total.append(tabela)
  
  display (tabela_total)


# ------------

tabela_produtos = tabela_total.groupby("Produto").sum()
display (tabela_produtos)
produtos_mais_vendidos = tabela_produtos[["Quantidade Vendida","Preco Unitario"]]
display (produtos_mais_vendidos)
quantidade_vendida = tabela_produtos [["Quantidade Vendida"]]
display (quantidade_vendida)

#tabela faturamento

tabela_total["Faturamento"] = tabela_total ["Quantidade Vendida"] * tabela_total["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum()

#somente a tabela faturamento em ordem decrecente

tabela_faturamento = tabela_faturamento [["Faturamento"]].sort_values(by="Faturamento", ascending = False)
display (tabela_faturamento)