import socket
s = socket.socket()
host = input('Por favor insira o endereço do host: ')
port = 8080
s.connect((host, port))

filename = input('por favor insira um nome de arquivo para o arquivo recebido: ')
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print('o arquivo foi recebido com sucesso.')
