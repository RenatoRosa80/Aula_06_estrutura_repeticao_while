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
    while  len(nome) <= 3:
        print(" Digitou um nome menor que 3 caracteres! Digite novamente! ")
        nome = input(" Informe seu nome: ")



    idade = int(input(" Informe sua Idade: ")) # entre 0 e 150
    if idade < 0 or idade > 150:
        print(" Idade inválida. Tente novamente! ")
        idade = int(input(" Informe sua Idade: ")) # entre 0 e 150


    salario = float(input(" Informe seu salário: ")) # maior que zero;
    if salario < 0:
        print(" Valor inválido. Digite seu Salário: ")
        salario = float(input(" Informe seu salário: ")) # maior que zero;


    sexo = str.upper(input(" Digite seu Sexo: M Masculino, F Feminino. "))
    if sexo != "M" and sexo != "F": 
        print(" Dados invalidos. Por favor informe novamente seu sexo.")
        sexo = str.upper(input(" Digite seu Sexo: M Masculino, F Feminino. "))


    estado_civil = str.upper(input(" Informe seu estado civil: ' S Solteiro ', ' C Casado ', 'V Viuvo', 'D Divorciado ' "))
    while estado_civil not in ("S", "C", "V", "D")  :
        print(" Caracteres invalidos. Insira norevamente seu Estado Civil!")
    else:
        print(" Dados aceitos! Obrigado. ")
        break


