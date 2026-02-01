# exemplo de funções

# funções locais
# exemplo colocando a variavel nome dentro da função e tentando chamar fora da função
# não funciona por ser local
'''
def minha_funcao():
    nome = 'juliano'
    print('Esta é uma função no python')
minha_funcao()
print(nome)
'''

# funções globais
# exemplo colocando a variável nome conmpleto fora da função e tentando chamar dentro da função 
# funciona por ser global
nome = 'juliano'

def minha_funcao():
    print(f'Este é o meu nome: {nome}')
minha_funcao()