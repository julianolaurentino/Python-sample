# %%
import json

alunos = json.read(open('Alunos.json', 'r'))

for aluno in alunos:

  print("Nome: ", aluno.nome, " - Matricula: ", aluno.matricula)
# %%
