"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

# ENTRADAS DE DADOS:
while True:
    nome = input(" Informe seu nome: ") # maior que 3 caracteres;
    while  len(nome) < 3:
        nome = input(" Informe seu nome: ")
        print(" Digitou um nome menor que 3 caracteres! Digite novamente! ")


    idade = int(input(" Informe sua Idade: ")) # entre 0 e 150
    if idade < 0 or idade > 150:
        print(" Idade inválida. Tente novamente! ")

    salario = float(input(" Informe seu salário: ")) # maior que zero;
    if salario < 0:
        print(" Valor inválido. Digite seu Salário: ")

    sexo = str.upper(input(" Digite seu Sexo: M Masculino, F Feminino. "))
    if sexo != "M" and sexo != "F": 
        print(" Dados invalidos. Por favor informe novamente seu sexo.")

    estado_civil = str.upper(input(" Informe seu estado civil: ' S Solteiro ', ' C Casado ', 'V Viuvo', 'D Divorciado ' "))
    if estado_civil != "S" or estado_civil != "C" or estado_civil != "V" or estado_civil != "D":
        print(" Caracteres invalidos. Insira novamente seu Estado Civil!")
    else:
        print(" Dados aceitos! Obrigado. ")
        break


