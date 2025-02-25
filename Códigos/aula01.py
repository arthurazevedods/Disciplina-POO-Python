def calcularMedia(av1, av2, av3):
    soma = av1 + av2 + av3
    media = soma/3

    print(media)

def opcao1():
    print('apertou na opcao1')

def opcao2():
    print('apertou na opcao2')
    
def menu():
    sair = 0 #condicao de saída
    while(sair == 0):
        opcao = input("Digite um numero (1 ou 2):") #entrada de dados
        if(opcao == "1"):
            opcao1()
        elif(opcao == "2"):
            opcao2()
        elif(opcao == "0"):
            sair = 1
        

menu()
#calcularMedia(7 , 5 , 10)
