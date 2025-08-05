"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
# ENTRADA
while  True:
    user = input(" Informe o nome do usuário: ")
    password = (input(" Informe seu Password: "))

    if user == password:
        print(" Usuário e Senha não podem ser iguais!")
    else:
        print(" Dados corretos!")
        break
    
   