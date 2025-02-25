#lista de jogos
jogos = [
    ("The Legend of Zelda", 25), 
    ("The Last Of Us", 20), 
    ("Call Of Duty", 20), 
    ("God of War", 30),
    ("Red Dead Redemption 2", 35), 
    ("Bioshock", 20), 
    ("Fifa", 25), 
    ("Pokémon", 30), 
    ("Mortal Kombat", 28)
]

alugados = [] #lista de alugados (vazia)

#função que mostra uma lista
def mostrar_lista(lista, titulo):
    print(f"\n=== {titulo} ===")
    if lista:
        for i, (nome, preco) in enumerate(lista):
            print(f"[{i}] {nome} - R$ {preco}/dia")
    else:
        print("Nenhum jogo disponível.")

while True:
    print("\n=========")
    print("Bem-vindo à locadora de jogos da 306!")
    print("=========")
    op = int(input("0 - Mostrar catálogo | 1 - Alugar | 2 - Devolver | 3 - Sair\n"))

    if op == 0:
        mostrar_lista(jogos, "Catálogo de Jogos")

    elif op == 1:
        mostrar_lista(jogos, "Catálogo de Jogos")
        cod_jogo = int(input("Escolha o código do jogo: "))
        dias = int(input("Quantos dias deseja alugar? "))

        nome, preco = jogos[cod_jogo]
        total = dias * preco
        print(f"\nVocê escolheu {nome} por {dias} dias. Total: R$ {total}. Confirmar? (0 - SIM | 1 - NÃO)")

        if int(input()) == 0:
            alugados.append(jogos.pop(cod_jogo))
            print(f"Parabéns, você alugou {nome} por {dias} dias.")

    elif op == 2:
        if not alugados:
            print("Não há jogos para devolver.")
        else:
            mostrar_lista(alugados, "Jogos Alugados")
            cod = int(input("Escolha o código do jogo para devolver: "))
            jogos.append(alugados.pop(cod))
            print("Obrigado por devolver o jogo.")

    elif op == 3:
        print("Até logo!")
        break