# %%
import pandas as pd
df = pd.read_csv('../data/transacao_produto.csv')
df


# %%
filtro = (df['idProduto'] == 5) | (df['idProduto'] == 11) 
df

# %%
#isin é parecido com IN do SQL
df['idProduto'].isin([5,11])
df[filtro]
# %%
