"""
Exercicios para fixação nivel basico
Laços, variáveis e funções
"""

"""
# Crie um programa de soma simples

def calculadora_simples():
    print("Calculadora simples")
    primeiro_numero = int(input("Digite o primeiro numero: "))
    segundo_numero = int(input("Digite o segundo numero: "))
    soma = primeiro_numero + segundo_numero
    print(f"A soma de {primeiro_numero} com {segundo_numero} é {soma}")


calculadora_simples()
"""


# Crie uma calculadora avançada
def calculadora_avancada():
    while True:
        print("Calculadora avançada")
        primeiro_numero = int(input("Digite o primeiro numero: "))
        segundo_numero = int(input("Digite o segundo numero: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            resultado = primeiro_numero + segundo_numero
        elif operacao == "-":
            resultado = primeiro_numero - segundo_numero
        elif operacao == "*":
            resultado = primeiro_numero * segundo_numero
        elif operacao == "/":
            resultado = primeiro_numero / segundo_numero
        elif operacao == "sair":
            break
        else:
            print("Operação inválida")
            return
        print(
            f"O resultado de {primeiro_numero} {operacao} {segundo_numero} é {resultado}"
        )


calculadora_avancada()
