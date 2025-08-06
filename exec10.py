"""
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de 
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do
país B, mantidas as taxas de crescimento.
"""
#ENTRADAS
populacao_a = 80000
populacao_b = 200000

#TAXA POPULACAO
taxa_populacao_a = 0.03
taxa_populacao_b = 0.015
anos = 0
#PROCESSAMENTO

while populacao_a < populacao_b:
    anos += 1
    populacao_a_taxa = populacao_a * taxa_populacao_a
    nova_populacao_a = populacao_a + populacao_a_taxa
    
    print(f"População de A: {int(populacao_a)}")
    print(f"População de B: {int(populacao_b)}")
    print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")

    break

