# Classe Livro
# Atributos: nome, autor, genero, numeroPaginas - variáveis
class Livro():
    def __init__(self, nome, autor, genero, numeroPaginas):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.numeroPaginas = numeroPaginas

senhorDosAnéis = Livro("Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1178)
crimeECastigo = Livro("Crime e Castigo", "Fiódor Dostoiévski", "Romance", 430)