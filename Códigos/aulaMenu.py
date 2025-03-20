series = [
    ("The Wire", 25), 
    ("The Office", 20), 
    ("Breaking Bad", 20), 
    ("The Sopranos", 30),
    ("Mr. Robot", 35), 
    ("Game Of Thrones", 20), 
    ("Fullmetal Alchmist", 25), 
    ("Jujutsu Kaisen", 30), 
    ("Frieren", 28),
    ("Attack On Titan", 28)
]

alugados = []

opcao = 1
print("\n=========")
print("Bem-vindo à locadora de séries da 306!") 
while (opcao != 0):
    print("\n=========")
    op = (input("0 - Sair \n1 - Mostrar catálogo \n2 - Mostrar alugados\n"))

    if(opcao == 0):
        print("Até logo!")
        break
    elif(opcao == 1):
        print("\n=========")
        print("Catálogo de Séries") 
        print(series)
    elif(opcao == 2):
        print("\n=========")
        print("Alugados")
        #verificação se alugados está vazio
        if(len(alugados)>0):
            print(alugados)
        else:
            print("Nenhuma série alugada")