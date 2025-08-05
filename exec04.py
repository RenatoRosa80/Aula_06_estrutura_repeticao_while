"""
4. Faça um Programa que verifique se uma letra digitada é 
vogal ou consoante.
"""
#Variables:
while True:
    letra_lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
    letra = str.lower(input(" Digite uma letra: "))
    if letra not in letra_lista:
        print(" O dado informado nao é uma Letra ")
        letra = str.lower(input(" Por favor, digite uma letra: "))
    break

    