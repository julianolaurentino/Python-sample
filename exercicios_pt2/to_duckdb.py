# %%
import pandas as pd
import duckdb 

INPUT_PATH = '/home/obzen/Documentos/workspace/dataset/googleplaystore_user_reviews.csv'
OUTPUT_PATH = '/home/obzen/Documentos/workspace/dataset/googleplaystore.duckdb'
print('Reading dataset...')
df = pd.read_csv(INPUT_PATH)
print('Dataset read successfully!')


# criar banco de dados DuckDB
print('Creating DuckDB database...')
con = duckdb.connect(OUTPUT_PATH)
print('DuckDB database created successfully!')
# %%