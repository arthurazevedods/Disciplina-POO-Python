a = 0

while a < 10:
    print(a)
    if a == 5:
        print("Número 5 encontrado!")
        break  # Encerra o loop quando a variável 'a' é igual a 5
    a += 1
print("Fim do loop")