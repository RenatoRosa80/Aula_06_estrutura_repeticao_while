"""
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B
seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do país
B, mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar as populações
e as taxas de crescimento iniciais. Valide a entrada e permita repetir
a operação.
"""
#ENTRADAS
populacao_a = int(input(" informe o número de Habitantes: "))
populacao_b = int(input(" informe o número de Habitantes: "))


#TAXA POPULACAO
taxa_populacao_a = 0.03
taxa_populacao_b = 0.015
anos = 0
#PROCESSAMENTO
if populacao_a > populacao_b:
    print(" Populacao A já é maior que a Populacao B!") 
while populacao_a < populacao_b:
    
    populacao_a += populacao_a * taxa_populacao_a
    populacao_b += populacao_b * taxa_populacao_b
    anos += 1
    
    print(f"População de A: {int(populacao_a)}")
    print(f"População de B: {int(populacao_b)}")
    print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a do país B. ")
    
