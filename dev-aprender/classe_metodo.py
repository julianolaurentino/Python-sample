'''

classe = Classes em Python são moldes que definem atributos (dados) e métodos (comportamentos) para criar objetos
__init__ = consultor que serve para criar a funcionalidade inicial que a classe terá
self = acessar as propriedades de uma instância
instância = é um objeto individual criado a partir de uma classe

'''


# Modelo para criar novas instancias
# marca, memoria ram, placa de video

class computador:
    def __init__(self):
        self.marca = 'Positivo'
        self.memoria_ram = '2gb'
        self.placa_video = 'nvidia'
    pass

computador1 = computador()
# print(computador1.marca)
computador2 = computador()
computador3 = computador()
print(computador1.marca, computador1.memoria_ram, computador3.placa_video)


# Deixando a classe dinâmica
class computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video    
    pass
computador1 = computador('asus','4gb','nvidea')
computador2 = computador('positivo','12gb','geforce')
computador3 = computador('dell','8gb','atm')
print(computador1.marca, computador1.memoria_ram, computador1.placa_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_video)