idade = int(input('Digite sua idade: '))

def idade_jovem():
    if idade >= 18:
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade.')


def idade_adulta():
    if idade >= 60:
        print('Você é idoso.')
    else:
        print('Você é adulto.')


def idade_idoso():
    if idade >= 80:
        print('Você é muito idoso.')
    else:
        print('Você é idoso.')
