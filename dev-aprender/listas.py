# listas

precos = [20,10,40]
print(precos[1]) # acessando por indice

print(precos.index(10))

# Acrescentando dados dentro da lista
salarios = [2500, 5000, 7000]
salario_usuario = float(input('Digite o seu salário: '))
salarios.append(salario_usuario)
print(f'Salários atualizados: {salarios}')


# Desafio
# gastos totais com pagamento de salários
# dado uma lista de salários, calcule o total pago a todos os funcionários
salarios_funcionarios = [1300, 2000, 3400, 5000]
total_gastos = sum(salarios_funcionarios)
print(f'Total gasto com salários: R$ {total_gastos}')