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
    
    
def download():
    arquivo = input('Nome do arquivo: ')
    fonte = (f'C:\\Users\CTRC2-M\Documents\server\\{arquivo}')
    usuario = input('Nome do usuario: ')
    if usuario in usuarios:
        destino = (f'C:\\Users\CTRC2-M\Documents\\{usuario}')
        shutil.copy(fonte, destino)
    else:
        print('Usuário não cadastrado.')

def uplaod():
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
1-cadastrar
2-login
3-nome do host
4-download do servidor
5-enviar arquivo para o servidor
    ''')
    op = int(input('opção: '))
    if op == 1:
        cadastrar_usuario()
    elif op == 2:
        login()
    elif op == 3:
        host()
    elif op == 4:
        dowload()
    elif op == 5:
        upload()
    else:
        print('Opção inválida.')
