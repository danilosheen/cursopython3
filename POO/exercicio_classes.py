# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
    
    
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._modelo_carro = None
        
        
        
motor1 = Motor('Motor v8')
motor2 = Motor('Motor 1.0')

carro1 = Carro('Ferrari moldel 2')
carro2 = Carro('Gol')

fabricante1 = Fabricante('Volksvagem')
fabricante2 = Fabricante('Ferrari')

carro1.fabricante = fabricante2
carro1.motor = motor1

carro2.fabricante = fabricante1
carro2.motor = motor2

print(f'Modelo do Carro: {carro1.nome}, Motor do carro: {carro1.motor.nome}, Fabricante: {carro1.fabricante.nome}')
print(f'Modelo do Carro: {carro2.nome}, Motor do carro: {carro2.motor.nome}, Fabricante: {carro2.fabricante.nome}')

