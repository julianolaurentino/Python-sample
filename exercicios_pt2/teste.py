# %%
import pandas as pd
import requests

url = "https://api.sampleapis.com/presidents/presidents"
df = pd.DataFrame(requests.get(url).json())
# df[['inicio','fim']] = df.yearsInOffice.str.split(' - ', expand=True)
df

# %%

base = "../../dataset/netflix_titles.csv"
df_netflix = pd.read_csv(base)
df_netflix.head()

# %%
