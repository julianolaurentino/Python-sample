# _*_ coding: utf-8 _*_

# Criando uma calculadora

a = int(input("Digite o Primeiro número aqui: "))
b = int(input("Digite o Segundo número aqui: "))
 
soma = a + b
subtracao = a - b 
multiplicacao = a * b 
divisao = a / b 
resto = a % b 

resultado = ('Soma: {soma}'
            '\nSubtração: {subtracao}'
            '\nMultiplicação: {multiplicacao}'
            '\nDivisão: {divisao}'
            '\nResto: {resto}'.format(soma=soma,
                                    subtracao=subtracao,
                                    multplicacao=multiplicacao,
                                    divisao=divisao,
                                    resto=resto,))
print(resultado)
 
