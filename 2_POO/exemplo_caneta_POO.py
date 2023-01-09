class Caneta:

    def __init__(self, cor, marca, ponta, tampada=True) :
        self.cor = cor
        self.marca = marca
        self.ponta = ponta
        self.tampada=tampada

    def escrever(self):
        if self.tampada:
            print(f'A caneta {self.marca} não pode escrever tampada')
            return

        print(f'A caneta {self.marca} de cor {self.cor} com ponta {self.ponta} está escrevendo...')
        

    def tampar(self):
        if self.tampada:
            print(f'A caneta {self.marca} já está tampada')
            return

        self.tampada=True
        print(f'A caneta {self.marca} foi tampada')

    def destampar(self):
        if not self.tampada:
            print('A caneta {} já está destampada')
            return

        self.tampada=False
        print(f'A caneta {self.marca} foi destampada')

c1 = Caneta('Azul', 'BIC', 0.7)
c2 = Caneta('Preta', 'Faber Castell', 1.0)

c1.escrever()
c2.escrever()
c1.destampar()
c1.escrever()
c1.tampar()
c1.escrever()
