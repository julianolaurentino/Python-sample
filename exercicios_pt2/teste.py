# %%
import pandas as pd
import pyarrow.parquet as pq

base = "../../dataset/anac_combinada/parquet/combinada2025-01.parquet"
df = pd.read_parquet(base)

# mostar todas as colunas no dataframe
pd.set_option("display.max_columns", None)
df.head()
# %%
