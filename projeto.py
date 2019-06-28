import os
import socket
import shutil
users = {'phablo': ['123'], 'cristian': ['123']}


def add_user():
    user = input('usuário: ')
    if user not in users:
        password = input('senha: ')
        users[user] = [password]
        os.mkdir(f'C:\\Users\CTRC2-M\Documents\server\\{user}')
    else:
        print('Nome de usuário indisponível.')


def login():
    login = input('login: ')
    password = input('senha: ')
    if login in users and password == users[login][0]:
        print('Usuário logado com sucesso.')
    else:
        print('Usuário ou senha inexistente. Tente novamente.')


def host():
    x = socket.gethostname()
    host = x.split('-')
    print(host[0])
    
    
def download():
    file_name = input('Nome do arquivo: ')
    source = (f'C:\\Users\CTRC2-M\Documents\server\\{file_name}')
    user = input('Nome do usuario: ')
    if user in users:
        destination = (f'C:\\Users\CTRC2-M\Documents\\{user}')
        shutil.copy(source, destination)
    else:
        print('Usuário não cadastrado.')


def upload():
    file_name = input('Nome do arquivo: ')
    user = input('Nome do usuário que irá fazer o uplaod: ')
    if user in users:
        source = (f'C:\\Users\CTRC2-M\Documents\\{user}\\{file_name}')
        destination = (f'C:\\Users\CTRC2-M\Documents\server')
        shutil.copy(source, destination)
    else:
        print('Usuário não cadastrado.')

        
def listing():
    user = input('Usuário: ')
    files = os.listdir(f'C:\\Users\CTRC2-M\Documents\server\\{user}')
    for i in files:
        print(i)
    

while True:
    print('''
1-Cadastrar usuário
2-Login
3-Download de arquivos da nuvem
4-Enviar arquivo para a nuvem
    ''')
    op = int(input('opção: '))
    if op == 1:
        add_user()
    elif op == 2:
        login()
    elif op == 3:
        download()
    elif op == 4:
        upload()
    else:
        print('Opção inválida.')
