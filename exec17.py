"""
Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.

Altere o programa anterior para mostrar no final a soma dos números.
"""

#ENTRADA

num1 = int(input(" Informe o primeiro número inteiro: "))
num2 = int(input(" Informe o segundo númnero inteiro: "))
soma = 0
for i in range(num1,num2 + 1):
    print(i,  end=",")
    soma += i
    print(f"\n A soma dos números é {soma}")
    