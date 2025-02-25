class Carro:
    def __init__(self, nome, marca, ano, diaria, alugado=False):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.diaria = diaria
        self.__alugado = alugado
        self.valor_aluguel = 0
        
    def verInformacoes(self):
        print("\nInformações do Carro:")
        print("Nome:", self.nome)
        print("Marca:", self.marca)
        print("Ano:", self.ano)
        print("Valor da diária: R$", self.diaria)
        if(self.__alugado):
            print("Está alugado")
            print("Valor Total do Aluguel: R$", self.valor_aluguel)
        else:
            print("Está disponível")
        

    def mudarStatusAluguel(self):
        self.__alugado = not self.__alugado
    
    def alugar(self, dias):
        self.valor_aluguel = self.diaria * dias
        self.mudarStatusAluguel()
        return self.valor_aluguel
    
    def devolver(self):
        if(self.__alugado):
            
            print("\nO valor total foi: R$", self.valor_aluguel )
            print("Carro devolvido")
            self.mudarStatusAluguel()
        else:
            print("\nO carro não estava alugado")


etios = Carro("Etios", "Toyota", 2020, 1500)
etios.verInformacoes()

hilux = Carro("Hilux", "Toyota", 2023, 2500)
hilux.verInformacoes()

hilux.alugar(5)
hilux.verInformacoes()

hilux.devolver()
hilux.devolver()

