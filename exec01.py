"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.

"""

while True:
    nota = int(input("Insira uma Nota entre [0 e 10]: " ))
    if nota < 0 or nota > 10:
        print(" Digite um valor válido! ")
    else:
        print(" Você digitou um valor válido! ")
        break
        
        

