
class Listas:
    def __init__(self):
        self.listas=[]

    def AdicionarAlunos(self):
        self.nome=input('Nome aluno: ')
        self.matricula=input('Matrícula: ')
        self.novaLista= {
            "nome": self.nome, 
            "matricula": self.matricula
        }
        self.listas.append(self.novaLista)

    def RemoverAlunos(self):
        self.excluir=input('Matrícula a ser excluida: ')

        for i in range (len(self.listas)):
            if self.listas[i]['matricula']==self.excluir:
                del self.listas[i]

    def AtualizarAlunos(self):
        self.atualizar=input('Matricula a atualizar: ')
        for i in range (len(self.listas)):
            if self.listas[i]['matricula']==self.atualizar:
                self.listas[i]['nome']=input('Novo nome: ')

    def VerAlunos(self):
        print(self.listas)






#---------------------------------------------------------------------------------
listaAlunos=Listas()
listaAlunos.AdicionarAlunos()
listaAlunos.AdicionarAlunos()
listaAlunos.AdicionarAlunos()
listaAlunos.VerAlunos()
listaAlunos.RemoverAlunos()
listaAlunos.VerAlunos()
