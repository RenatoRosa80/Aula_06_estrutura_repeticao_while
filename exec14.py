"""
Faça um programa que leia 5 números e informe a soma e a média dos 
números.

"""
#ENTRADA
num1 = float(input(" Informe um número: "))
num2 = float(input(" Informe um número: "))
num3 = float(input(" Informe um número: "))
num4 = float(input(" Informe um número: "))
num5 = float(input(" Informe um número: "))

soma = num1 + num2 + num3 + num4 + num5
print(f" A soma dos numeros é {int(soma)} ")

media = soma / 5
print(f" A média dos numeros é {int(media)} ")