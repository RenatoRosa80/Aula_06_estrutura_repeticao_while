"""
9. Faça um Programa que leia três números e mostre-os em 
ordem decrescente
"""
# Leitura dos três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


numeros = [num1, num2, num3] # Coloca os números em uma lista


numeros.sort(reverse=True) # Ordena a lista em ordem decrescente

# Exibe os números ordenados
print("Números em ordem decrescente:")
print(numeros[0], numeros[1], numeros[2])
