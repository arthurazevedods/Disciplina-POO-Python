class Livro():
    def __init__(self, nome, autor, numeroPaginas, lido = False):
        self.nome = nome
        self.autor = autor
        self.numeroPaginas = numeroPaginas
        self.lido = lido

    def exibirInfos(self):
        print (f"Nome: {self.nome}")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.numeroPaginas}")
        print(f"Lido: {self.lido}")
        print("===================================")
    def marcarLido(self):
        self.lido = True
        print(f"Livro {self.nome} lido com sucesso!")

# Criando instâncias da classe Livro
livro1 = Livro("Senhor dos Anéis", "J.R.R. Tolkien", 1178)
livro2 = Livro("Crime e Castigo", "Fiódor Dostoiévski", 430)
livro1.exibirInfos()
livro2.exibirInfos()
livro1.marcarLido()
livro1.exibirInfos()