import os
import socket
import shutil
usuarios = {'phablo': ['123'], 'cristian': ['123']}


def add_user():
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
    
    
def download():
    arquivo = input('Nome do arquivo: ')
    fonte = (f'C:\\Users\CTRC2-M\Documents\server\\{arquivo}')
    usuario = input('Nome do usuario: ')
    if usuario in usuarios:
        destino = (f'C:\\Users\CTRC2-M\Documents\\{usuario}')
        shutil.copy(fonte, destino)
    else:
        print('Usuário não cadastrado.')


def upload():
    arquivo = input('Nome do arquivo: ')
    usuario = input('Nome do usuário que irá fazer o uplaod:')
    if usuario in usuarios:
        fonte = (f'C:\\Users\CTRC2-M\Documents\\{usuario}\\{arquivo}')
        destino = input('Destino: ')
        shutil.copy(fonte, destino)
    else:
        print('Usuário não cadastrado.')
    

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
