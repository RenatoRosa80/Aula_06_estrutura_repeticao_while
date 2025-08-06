"""
Faça um programa que leia 5 números e informe o maior número.

"""
num1 = float(input(" Informe um número: "))
num2 = float(input(" Informe um número: "))
num3 = float(input(" Informe um número: "))
num4 = float(input(" Informe um número: "))
num5 = float(input(" Informe um número: "))

#Condititions

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print(" O Número 1 é o maior dos 5 números informados! ")
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print(" O número 2 é o maior dos 5 números informados! ")
elif num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5 :
    print(" O número 3 é o maior dos 5 números informados! ")
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 :
    print(" O número 4 é o maior dos 5 números informados! ")
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4 :
    print(" O número 5 é o maior dos 5 números informados! ")
else:
    print(" Os números informados sao iguais! ")
