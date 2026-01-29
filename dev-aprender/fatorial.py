# projeto fatorial de numero

# crie um programa que recebe um numero e imprime o seu fatorial

fatorial = 1
numero = int(input('Digite um numero: '))

for num in range(1, numero + 1):
    fatorial *= num
    print(f'A sequencia do fatorial de {numero} é: {fatorial}')
print(fatorial)