class Material:
    def __init__(self,titulo,autor_ou_editora):
        self.titulo=titulo
        self.autor_ou_editora=autor_ou_editora
    def exibir_informacoes(self):
        print('Titulo: ',(self.titulo))
        print('Autor:',(self.autor_ou_editora))

class Livro(Material):
    def __init__(self,titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero=genero
    
    def exibir_informações(self):
        print('----------------------------------')
        super().exibir_informacoes()
        print('Genero: ',(self.genero))
        print('----------------------------------')
        

class Revista(Material):
    def __init__(self,titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao=edicao
    
    def exibir_informações(self):
        print('----------------------------------')
        super().exibir_informacoes()
        print('Edição: ',(self.edicao))
        print('----------------------------------')

#-------------------------------------------------------------------------
        
TurmaDaMonica=Revista('Cebolinha','Mauricio de Sousa','Quadrinhos')
DomQuixote=Livro('DomQuixote','Joao','Aventura')
TurmaDaMonica.exibir_informações()
DomQuixote.exibir_informações()
