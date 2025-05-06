# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

filtro = clientes['qtdePontos'] == 0
clientes[filtro]