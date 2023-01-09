class Carro:
    def __init__(self, nome, marca, cor):
        self.nome = nome
        self.marca = marca
        self.cor = cor

    
    def acelerar(self):
        print('Estou acelerando')
        print(self.nome)
        print(self.marca)
        print(self.cor)
        print()
    

    def frear(self):
        print('Estou freando')
        print(self.nome)
        print(self.marca)
        print(self.cor)
        print()

fusca = Carro('fusca', 'Volkswagen', 'Amarelo')
#alternativa de execução de um método
Carro.acelerar(fusca)

gol = Carro('Gol', 'Volksvagem', 'Vermelho')
#alternativa de execução de um método
Carro.acelerar(gol)

fusca.acelerar()
gol.acelerar()
gol.frear()
fusca.frear()
