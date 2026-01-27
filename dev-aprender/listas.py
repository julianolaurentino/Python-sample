# listas

precos = [20,10,40]
print(precos[1]) # acessando por indice

print(precos.index(10))

# Acrescentando dados dentro da lista
salarios = [2500, 5000, 7000]
salario_usuario = float(input('Digite o seu salário: '))
salarios.append(salario_usuario)
print(f'Salários atualizados: {salarios}')