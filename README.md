# 🐍 Exercícios em Python  

Este repositório contém diversos exercícios em Python, abordando diferentes níveis de dificuldade e conceitos fundamentais da linguagem.  


# Pilares do aprendizado 

É necessário focar nos seguintes pilares e suas estruturas:
* Lógica
* Estrutura de pensanmento
* Resolução de problemas
* Arquiterura de software

# Fundamentos de Python (obrigatório, mas focado)
Você não precisa virar dev de software, mas precisa escrever código robusto e legível.

Essencial:
Tipos básicos: int, float, str, list, dict, set

Controle de fluxo:

if / else

for, while

break, continue

Funções:

def

argumentos nomeados

*args, **kwargs

Compreensão de listas e dicionários

Manipulação de erros: Try, Except

# Manipulação e Estruturação de Dados
Aqui está o coração do seu trabalho quando lidando com bases diferentes.

Pandas (nível intermediário/avançado)
Não só saber usar, mas entender impacto e boas práticas.

Essencial:
Leitura de fontes diversas:

read_csv, read_excel

read_parquet

read_sql

JSON aninhado

Limpeza e padronização:

astype

fillna, dropna

normalização de strings

Joins complexos:

merge (left, right, inner, outer)

Agregações:

groupby

janelas simples

Trabalhar com datas:

to_datetime

timezone

granularidade (dia, mês, hora)

# Trabalhar com Dados Semi-estruturados (MUITO importante)
Quando você fala em estruturar bases diferentes, isso é central.

JSON / APIs
Leitura e parsing de JSON aninhado

Flatten de estruturas complexas

Paginação de API

Autenticação (token, basic auth)

Exemplo mental:

“Uma API retorna pesquisa, perguntas e respostas em níveis diferentes → você precisa normalizar isso em tabelas relacionais”

Ferramentas:

json

requests

pandas.json_normalize

# SQL + Python (engenharia de verdade acontece aqui)
Python não substitui SQL, ele orquestra SQL.

Essencial:
Executar SQL via Python:

sqlalchemy

psycopg2

pyodbc

Ler e escrever tabelas

Upsert (insert/update)

Controle de transações

💡 Mentalidade correta:

Transformações pesadas → SQL
Orquestração, validação, integração → Python

# Qualidade, Validação e Confiabilidade dos Dados
Muito negligenciado por analistas, central para engenharia.

Aprenda a:
Validar esquema:

colunas esperadas

tipos

Validar volume:

contagem mínima/máxima

Validar regras de negócio:

datas futuras

valores negativos inválidos

Ferramentas/conceitos:

assert

logs

bibliotecas como pandera ou great expectations

# Performance e Escalabilidade
Quando os dados crescem, Pandas sozinho sofre.

Próximos passos:
Parquet vs CSV

Leitura por chunks

DuckDB com Python

PyArrow

# Organização de Projetos e Pipelines
Aqui você começa a parecer engenheiro de dados de verdade

Essencial:
Estrutura de projeto:

project/
├── src/
├── scripts/
├── config/
├── logs/
└── README.md

Arquivos de configuração (.yaml, .env)

Logs (logging)

Scripts reutilizáveis (funções, módulos)

# Automação e Orquestração (nível profissional)
Você já tocou nisso com KNIME, Docker, .bat, então faz muito sentido.

Aprenda:
Rodar scripts via linha de comando

Variáveis de ambiente

Agendamento (cron, task scheduler)

Conceitos de Airflow / Prefect / Dagster (mesmo que não use ainda)

# Git e Versionamento (não negociável)
commit pequenos e claros

branches

versionar scripts de ETL
