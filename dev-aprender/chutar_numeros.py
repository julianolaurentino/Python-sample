# Desafio

# Escreva um programa que, ao iniciar, gere um valor aleatorio de 1 a 10 e permita
# que o usuário chute numero ate acertar p valor gerado

# o programa deve informar se o chute foi maior, menor ou igual ao valor aleatorio gerado no inicio

import random
numero_random = random.randint(1, 10)
numero_usuario = int(input('Chute um numero de 1 a 10: '))
while True:
    if numero_usuario > numero_random:
        print('Errou! Seu numero é maior.')
        numero_usuario = int(input('Chute novamente: '))
    elif numero_usuario < numero_random:
        print('Errou! Seu numero é menor.')
        numero_usuario = int(input('Chute novamente: '))
    else:    
        print('Parabens! Voce acertou!')    
        break