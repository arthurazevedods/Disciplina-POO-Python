class Person():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def showInfos(self):
        print('\nInformações da Pessoa:\n\tNome: ',self.nome,'\n\tIdade: ',self.idade)

pessoa = Person('Fulano', 27)

pessoa.showInfos()

print(pessoa.nome)