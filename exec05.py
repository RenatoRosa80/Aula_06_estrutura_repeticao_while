"""
5. Faça um programa para a leitura de duas notas parciais de 
um aluno. O programa deve calcular a média alcançada por 
aluno e apresentar: 
- A mensagem "Aprovado", se a média alcançada for maior ou 
igual a sete; 
- A mensagem "Reprovado", se a média for menor do que sete; 
- A mensagem "Aprovado com Distinção", se a média for igual 
a dez

"""
print("____________________________________")
print( " NOTAS FINAIS DO SEMESTRE '2025'")
print("____________________________________")
#ENTRADAS
nota1 = float(input(" Informe a primeira nota: "))
nota1_arredondada = round(nota1, 0)
nota2 = float(input(" Informe a Segunda nota: "))
nota2_arredondada = round(nota2, 0)
media_nota = (nota1 + nota2) / 2
media_arredondada = round(media_nota, 0)  # Arredonda para 1 casa decimal

print(f"Nota 1: {nota1_arredondada}")
print(f"Nota 2: {nota2_arredondada}")


#PROCESSAMENTO

"""A mensagem "Aprovado", se a média alcançada for maior ou 
igual a sete; 
"""
if media_nota >= 7 and media_nota < 10:
    print(f"A média foi de {media_arredondada} ")
    print(" Aprovado!")
#- A mensagem "Reprovado", se a média for menor do que sete; 
elif media_nota < 7:
    print(f"A média foi de {media_arredondada}" )
    print(" Reprovado! Estude mais.")
# - A mensagem "Aprovado com Distinção", se a média for igual a 10

elif media_nota == 10:
    print(f"A média foi de {media_arredondada}")
    print(" Aprovado com Distincao! Parabéns.")
else:
    print(" Dados inválidos. tente outra vez.")
    