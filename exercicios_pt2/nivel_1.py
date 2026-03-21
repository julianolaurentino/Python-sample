"""
Exercicios para fixação nivel basico ao avançado
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
"""

# Crie uma calculadora avançada

def calculadora_avancada():
    while True:
        print("Calculadora avançada")

        try:
            primeiro_numero = int(input("Digite o primeiro numero: "))
            segundo_numero = int(input("Digite o segundo numero: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue
        
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            resultado = primeiro_numero + segundo_numero
        elif operacao == "-":
            resultado = primeiro_numero - segundo_numero
        elif operacao == "*":
            resultado = primeiro_numero * segundo_numero
        elif operacao == "/":
            resultado = primeiro_numero / segundo_numero
        else:
            print("Operação inválida")
            
            while True:
                operacao = input("Digite uma operação válida novamente (+, -, *, /): ")
                if operacao in ["+", "-", "*", "/"]:
                    continue
                else:
                    print("Operação inválida. Encerrando a calculadora avançada.")
                    break
        
        print(f"O resultado de {primeiro_numero} {operacao} {segundo_numero} é {resultado}")
        continuar = input('Deseja continuar? (s/n): ')
        if continuar == 'n':
            print("Encerrando a calculadora avançada")
        elif continuar == 's':
            continue
        else:
            print("Entrada inválida. Encerrando a calculadora avançada.")  
        break
        
calculadora_avancada()