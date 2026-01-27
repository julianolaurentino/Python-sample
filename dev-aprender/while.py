# # laços de repetição While

'''
While condicao:
    codigo a ser executado
'''

# Programa que permite 3 tentativas, antes de fechar
tentativas = 0
while tentativas < 3:
    print('Tente novamente')
    tentativas = tentativas + 1

# Quando queremos que uma ação continue acontecendo, até que um 
# critério seja satisfeito
# so pode logar, se digitar a senha correta
senha = 0
while senha != '123456':
    senha = input('Digite a senha corretamente: ')
print('Login realizado com sucesso')

# Garantir que algo está preenchido
# Só deve continuar, quanddo o usuário informar seu nome
nome = ''
while nome == '':
    nome = input('Digite novamente o seu nome: ')
print(f'Bem vindo {nome}')