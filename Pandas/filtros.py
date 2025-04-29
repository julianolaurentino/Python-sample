# %%
import pandas as pd
df = pd.read_csv('../data/transacoes.csv')
df.head(5)

# %%
pontos = [10, 20, 30 ,40 
          ,50 ,60, 70, 80 ,90, 100]
filtro = []
valores_acima_50 = []
for i in pontos:
    if i >=50:
        filtro.append(i)
        #filtro.append(i>=50)
valores_acima_50
filtro

# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo","nah","mah"],
        "idade": [18, 30, 45],
        "uf": ["sp","rj","ce"],
    }
)
filtro = brinquedo["idade"] == 30
brinquedo[filtro]

# %%
#qtd de pontos acima de 50

df = pd.read_csv('../data/transacoes.csv')
df.head(5)

pontos_acima_50 = df['qtdePontos'] >= 50
df[pontos_acima_50]
# %%
#qtd de pontos acima de 50 e menor que 100
acima_50_abaixo_100 = (df['qtdePontos'] >= 50) * (df['qtdePontos'] < 100)
df[acima_50_abaixo_100]

# %%
#utilizando o "ou" |
acima_50_ou_abaixo_100 = (df['qtdePontos'] == 50) | (df['qtdePontos'] == 100)
df[acima_50_ou_abaixo_100]