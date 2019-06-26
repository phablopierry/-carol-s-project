import shutil

while True:
    fonte = input('Caminho da fonte: ')
    destino = input('Caminho do destino: ')
    shutil.copy(fonte, destino)
