import os
import socket
usuarios = {'phablo': ['123'], 'cristian': ['123']}


def cadastrar_usuario():
    usuario = input('usuário: ')
    if usuario not in usuarios:
        senha = input('senha: ')
        usuarios[usuario] = [senha]
        os.mkdir(f'/home/cristian/Música/{usuario}')
    else:
        print('Nome de usuário indisponível.')


def login():
    login = input('login: ')
    senha = input('senha: ')
    if login in usuarios and senha == usuarios[login][0]:
        print('Usuário logado com sucesso.')
    else:
        print('Usuário ou senha inexistente. Tente novamente.')


def host():
    host = socket.gethostname()
    x = host.split('-')
    print(x[0])

while True:
    print('''
1-cadastrar
2-login
3-nome do host    
    ''')
    op = int(input('opção: '))
    if op == 1:
        cadastrar_usuario()
    elif op == 2:
        login()
    elif op == 3:
        host()
    else:
        print('Opção inválida.')