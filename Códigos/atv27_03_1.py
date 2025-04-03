numero = 0
lista = []
while numero > -1:
    numero = int(input("Digite um número:"))
    if(numero > 0):
        lista.append(numero)

print("Os números positivos foram: ")
print(lista)

a = lista.pop(0)
print(a)
print(lista)
