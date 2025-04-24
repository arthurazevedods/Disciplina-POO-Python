#Função para Verificar Par ou Ímpar
#Crie uma função par_impar(num) que retorna:
#"Par" se o número for par, ou "Ímpar" 
# se for ímpar.

def EhPar(n):
    if n % 2 == 0:
        return f"{n} é par"
    else:
        return f"{n} é ímpar"

print(EhPar(7))
resul = EhPar(10)
print(resul)
print(resul)
