def calcularDesconto(preco, desconto):
    valor_final = preco - (preco*desconto)
    return valor_final
    

def seTemDesconto(nome,preco,desconto):
    print('\n')
    if(desconto > 0):
        valor_final = calcularDesconto(preco,desconto)
        print(nome,'tem o desconto de:',(desconto*100),'%')
        print('O valor final é:R${:.2f}'.format(valor_final))
    else:
        print(nome, 'não tem desconto')
        print('O valor final é:R${:.2f}'.format(preco))

nome_produto = "Camisa da Nike"
preco = 149.99
desconto = 0.05

seTemDesconto(nome_produto, preco, desconto)

nome_produto2 = "Copo Stanley"
preco = 200.00
desconto = 0

seTemDesconto(nome_produto2, preco, desconto)




