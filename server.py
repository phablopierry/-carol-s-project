import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print('esperando por conexões de entrada')
conn, addr = s.accept()
print(addr, 'se conectou ao servidor')

filename = input('por favor digite o nome do arquivo: ')
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print('os dados foram transmitidos com sucesso')