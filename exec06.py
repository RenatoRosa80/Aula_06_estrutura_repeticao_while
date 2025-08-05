"""
6. Faça um Programa que leia três números e mostre o maior 
deles
"""
#ENTRADA
num1 = float(input(" Informe o primeiro número: "))
num2 = float(input(" Informe o segundo número: "))
num3 = float(input(" Informe o terceiro número: "))

#Condititions

if num1 > num2 and num1 > num3:
    print(" O Número 1 é o maior dos 3 números informados! ")
elif num2 > num1 and num2 > num3:
    print(" O número 2 é o maior dos 3 números informados! ")
elif num3 > num2 and num3 > num1:
    print(" O número 3 é o maior dos 3 números informados! ")
else:
    print(" Os números informados sao iguais! ")
