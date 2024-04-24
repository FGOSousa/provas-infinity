class Elevador():
    def __init__(self, totalCapacidade, atualCapacidade, totalAndares, andarAtual):
        self.totalCapacidade=totalCapacidade
        self.atualCapacidade=atualCapacidade
        self.totalAndares=totalAndares
        self.andarAtual=andarAtual

    def subir(self):
        if self.andarAtual<self.totalAndares:
            print('Elevador subindo')
            self.andarAtual+=1
            print(self.andarAtual)
        elif self.andarAtual==self.totalAndares:
            print('Elevador no último andar')
    
    def descer(self):
        if self.andarAtual>0:
            print('Elevador descendo')
            self.andarAtual-=1
            print(self.andarAtual)
        elif self.andarAtual==0:
            print('Elevador no andar térreo')

    def entrar(self):
        if self.atualCapacidade<self.totalCapacidade:
            print('Entrando uma pessoa')
            self.atualCapacidade+=1
            print('Capacidade atual: ',(self.atualCapacidade))
        elif self.atualCapacidade==self.totalCapacidade:
            print('Elevador cheio')
    
    def sair(self):
        if self.atualCapacidade>0:
            print('Saindo uma pessoa')
            self.atualCapacidade-=1
            print('Capacidade atual: ',(self.atualCapacidade))
        elif self.atualCapacidade==0:
            print('Elevador vazio')

#------------------------------------------------------------------------------------
            
elevadorL=Elevador(6,3,10,5)
elevadorL.entrar()
elevadorL.entrar()
elevadorL.entrar()
elevadorL.entrar()
elevadorL.descer()
elevadorL.descer()
elevadorL.descer()
elevadorL.descer()
elevadorL.descer()
elevadorL.descer()
elevadorL.sair()
elevadorL.sair()
elevadorL.sair()
elevadorL.sair()
elevadorL.sair()
elevadorL.sair()
elevadorL.sair()
elevadorL.entrar()
elevadorL.entrar()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.subir()
elevadorL.entrar()
elevadorL.entrar()
elevadorL.entrar()
elevadorL.entrar()
elevadorL.entrar()




        