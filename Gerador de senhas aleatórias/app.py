import random
from termcolor import colored
import itertools
import sys
from time import sleep

while True:
    print(colored('-'*10 + 'Gerador de Senhas Aleatórias' + '-'*10, 'green'))

    letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
    letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']
    simbolos = ['!', '@', '#', '$', '%']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # 1. Escolha do Comprimento da Senha.
    comprimento_senha = int(input('Quantos caracteres deseja ter em sua senha? '))

    # 2. Escolha dos Componentes da Senha.
    componentes_senha = input('Deseja incluir letras maiúsculas (1), minúsculas (2), números (3), símbolos (4)? '
                              'Digite os números separados por vírgula, ex: 1,2,3: ').split(',')

    # 3. Geração da Senha Aleatória.
    caracteres_possiveis = []

    # Verificando as escolhas do usuário e adicionando os caracteres possíveis à lista.
    if '1' in componentes_senha:
        caracteres_possiveis += letras_maiusculas
    if '2' in componentes_senha:
        caracteres_possiveis += letras_minusculas
    if '3' in componentes_senha:
        caracteres_possiveis += numeros
    if '4' in componentes_senha:
        caracteres_possiveis += simbolos

    # Adicionando um spinner para mostrar que a senha está sendo gerada.
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    print("Gerando senha, por favor aguarde...", end="")
    
    for _ in range(20):  # Simula um breve tempo de geração da senha
        sys.stdout.write(next(spinner))   # Mostra o próximo caractere do spinner
        sys.stdout.flush()  # Garante que o caractere é mostrado imediatamente
        sleep(0.1)  # Atraso para dar a sensação de "giro"
        sys.stdout.write('\b')  # Apaga o último caractere

    # Gerando a senha aleatória com base nos caracteres possíveis.
    senha = ''.join(random.choices(caracteres_possiveis, k=comprimento_senha))

    print(f'\nSua senha é: {senha}')
    repetir = input('Deseja gerar outra senha (s/n)? ')
    if repetir.lower() != 's':
        break
