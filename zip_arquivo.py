import os
import zipfile
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


fantasy_zip = zipfile.ZipFile('C:\\Users\\CTRC3-T\\Desktop\\phablo\\archive.zip', 'w')

for folder, subfolders, files in os.walk('C:\\Users\\CTRC3-T\\Desktop\\phablo'):

    for file in files:
        if file.endswith(''):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Users\\CTRC3-T\\Desktop\\phablo'), compress_type = zipfile.ZIP_DEFLATED)

fantasy_zip.close()
#credenciais e login no servidor
remetente = 'lip.pratica'
senha     = 'L#P12345'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(remetente,senha)

#definicao das informacoes
destinatario = input('digite seu email: ')
assunto = 'ASSUNTO:enviando arquivos .zip'

corpo = 'segue em anexo os arquivos zipados, ao baixar renomeie o arquivo para .zip '

# Cria o documento com varias partes
msg = MIMEMultipart()
msg["From"] = input('Digite seu nome: ')
msg["To"] = destinatario
msg["Subject"] = assunto


# Colocando texto no corpo da mensagem.
msgText = MIMEText(corpo)
msg.attach(msgText)

# Anexa a imagem
Filename = input('digite o caminho e o nome da imagem e a extensão')
with open(Filename, 'rb') as f:
    arq_zip = MIMEImage(f.read(), name="arquivo_zipado.jpg") # Repare que e diferente do nome do arquivo local!
msg.attach(arq_zip)


# Envia!

server.sendmail(remetente, destinatario, msg.as_string()) #lembrar de usar a funcao as_string() na hora de enviar o email multipart
server.quit()
