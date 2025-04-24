class Person():
    def __init__(self, nome, idade):
        #o self é o atributo
        #nome e idade do init são as variáveis de chegam do construtor
        self.nome = nome 
        self.idade = idade
    
    #Método/Funções
    def Dormir(self):
        print(f"O(A) {self.nome} está dormindo")
    def Acordar(self):
        print(f"O(A) {self.nome} está acordado(a)")

#Criação de um objeto
alexandre = Person("Alexandre", 18) # chamando a função construtora

#Acesso as informações
print(alexandre.idade)
print(alexandre.nome)

#Criar outro objeto
helena = Person("Helena", 17)
print(helena.nome)

#Funções
carla = Person("Carla Vitória", 17)
carla.Dormir()
carla.Acordar()