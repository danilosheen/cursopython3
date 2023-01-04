class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'A câmera {self.nome} já está filmando!')
            return
            
        print(f'A câmera {self.nome} está filmando...')
        self.filmando = True
        
        
    def parar_filmar(self):
        if not self.filmando:
            print(f'A {self.nome} não está filmando!')
            return
        
        print(f'A câmera {self.nome} está parando de filmar...')
        self.filmando = False
        
        
    def fotografar(self):
        if self.filmando:
            print(f'A câmera {self.nome} não pode fotografar filmando!')
            return
        
        print(f'A câmera {self.nome} está fotografando...')

c1 = Camera('Canon')
c2 = Camera('Sony')
c3 = Camera('Nikon')

# c1.filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
c1.filmar()
c2.fotografar()


    