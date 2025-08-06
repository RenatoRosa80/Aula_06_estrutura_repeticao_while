"""
Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.
"""
#ENTRADA

num1 = int(input(" Informe o primeiro número inteiro: "))
num2 = int(input(" Informe o segundo númnero inteiro: "))

for i in range(num1,num2):
    print(i, end=",")
