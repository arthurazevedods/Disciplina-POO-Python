def EhPrimo(numero):
    ehprimo = True
    if numero < 2:
        ehprimo = False 
    else:
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = False
                break   
    return ehprimo




n = EhPrimo(5)
print(n)