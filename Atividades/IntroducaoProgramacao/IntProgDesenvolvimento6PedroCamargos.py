## Desenvolvimento 6 ##

'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''

def retornaIdade():
    while True:
        anoNascimento = input("Digite seu ano de nascimento: ")
        try:
            anoNascimento = int(anoNascimento)
            if anoNascimento < 1922 or anoNascimento > 2021:
                print('Ano inválido. Digite um ano entre 1922 e 2021.')
            else:
                return 2022 - anoNascimento
        except ValueError:
            print('Ano inválido. Digite um número.')

nome = input('Digite seu nome completo: ').strip()
idade = retornaIdade()

print(f'Olá, {nome}! Você completou ou completará {idade} anos em 2022.')