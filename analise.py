import pandas as pd

# Importando os dados da tabela
dados = pd.read_excel(
    'dados-aula-ia.xlsx',
    index_col = None,
    header=0,
    usecols = "C, ES, QJ")

# Criando o dataframe a partir dos dados importados
df = pd.DataFrame(dados)

# Formatando o dataframe
df_formatada = pd.DataFrame(
    columns = {
        "Nome": df["Nome do Estabelecimento"], 
        "Possui biblioteca?": df["2.5.1 Há local específico para biblioteca?"],
        "Alvarás de soltura": df["4.5 Movimentação no Sistema Prisional (total do período de referência) | Saídas | Alvarás de soltura | Total"],
    })

# Retirando os nulos
not_nulls = df_formatada.dropna()

# Medindo a relação a partir das colunas sem dados nulos.
#relacao = not_nulls["2.5.1 Há local específico para biblioteca?"].corr
#(not_nulls["4.5 Movimentação no Sistema Prisional (total do período de referência) | Saídas | Alvarás de soltura | Total"])

#print("A relação é de: {}".format(relacao))