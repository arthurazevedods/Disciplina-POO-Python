# Classe Série
# Atributos: nome, numeroTemporadas, numeroEpisodios, genero - variáveis
class Serie():
    def __init__(self, nome, numeroTemporadas, numeroEpisodios, genero):
        self.nome = nome
        self.numeroTemporadas = numeroTemporadas
        self.numeroEpisodios = numeroEpisodios
        self.genero = genero

got = Serie("Game of Thrones", 8, 73, "Fantasia")
breakingBad = Serie("Breaking Bad", 5, 62, "Drama")

# acessar atributos do objeto Game of Thrones
print(got.nome)
print("Número de temporadas:",got.numeroTemporadas)

# acessar atributos do objeto Breaking Bad
print(breakingBad.nome)
print("Número de temporadas:",breakingBad.numeroTemporadas)