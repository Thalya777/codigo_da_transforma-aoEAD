'''

Criar um sistema de biblioteca 

Class livro:

   produtos:
   livros, periodicos, jornal, maps, gibis, mangas.

   Class biblioteca (main):

   (processos)
   Ler,pesquisar, emprestar-devolução.

'''



class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        
    def __str__(self):
        status = "Disponivel" if self.disponivel else "indisponivel"
        return f" '{self.titulo}' - {self.autor} [status]"
    





class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livros(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo_procurando):
        for livro in self.livros:
            if livro.titulo == titulo_procurando:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empretimo de '{livro.titulo}' realizado")
                else:
                    print("Livro não encontrado no acervo")


biblioteca_municipal = Biblioteca()
livro1 = Livro("Dom quixote", "Miguel de Cervantes")
livro2 = Livro("O Principe", "Antoine de Saint-Exupéry")
livro3 = Livro("Dom casmurro", "Machado de Assis")
livro4 = Livro("It", "Stephen King") 

biblioteca_municipal.adicionar_livros(livro1)
biblioteca_municipal.adicionar_livros(livro2)
biblioteca_municipal.adicionar_livros(livro3)
biblioteca_municipal.adicionar_livros(livro4)

print(livro2)
biblioteca_municipal.emprestar_livro("O Principe")
print(livro2)

