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
filtro = brinquedo["idade"] > 30
brinquedo[["uf","nome"]]
