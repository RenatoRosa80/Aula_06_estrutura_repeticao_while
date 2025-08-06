"""
9. Faça um Programa que leia três números e mostre-os em 
ordem decrescente
"""


# Lendo os três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontrando a ordem decrescente
if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    maior = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1
else:
    maior = num3
    if num1 >= num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1

# Mostrando os números em ordem decrescente
print(f"Números em ordem decrescente: {maior}, {medio}, {menor}")

"""
Explicação:
1. O programa começa lendo três números do usuário.
2. Em seguida, verifica qual é o maior número entre os três.
3. Depois de identificar o maior, verifica a ordem dos outros dois.
4. Finalmente, imprime os números em ordem decrescente.
"""
