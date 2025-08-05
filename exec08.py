"""
8. Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a 
decisão é sempre pelo mais barato
"""
print("____________________________________")
print( " Bem vindos ao Mercado Minas é Aqui")
print("____________________________________")

#ENTRADA
produto1 = float(input(" informe o Valor do Produto 1 :"))
produto2 = float(input(" informe o Valor do Produto 2 : "))
produto3 = float(input(" informe o Valor do Produto 3 : "))
print(f" Valor do Produto 1: R${produto1}")
print(f" Valor do Produto 2 R${produto2}")
print(f" Valor do Produto 3: R${produto3}")


#PROCESSAMENTO

if produto1 < produto2 and produto1 < produto3:
    print(" Voce deve comprar o produto 1 pois é mais barato! ")
elif produto2 < produto1 and produto2 < produto3:
    print(" Voce deve comprar o produto 2 pois é mais barato! ")
elif produto3 < produto1 and produto3 < produto2:
    print(" Voce deve comprar o produto 3 pois é mais barato! ")
else:
    print(" Dados informados sao invalidos! ")