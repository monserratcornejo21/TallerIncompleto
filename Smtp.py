import socket
from RecEnv import enviar,recibir 

host = socket.gethostbyname('DESKTOP-6L6O5MA')
port = 25
ipv4 = socket.AF_INET
tcp  = socket.SOCK_STREAM
user = input

with socket.socket(ipv4,tcp) as conexion:
    conexion.connect((host, port))
    recibir(conexion)
    enviar(conexion,'HELLO ayredes.ddns.net')
    recibir(conexion)
    enviar(conexion,'MAIL FROM: {}'.format(host))
    recibir(conexion)
    enviar(conexion,'RCPT TO: {}'.format(user))
    recibir(conexion)
    enviar(conexion,'DATA')
    recibir(conexion)
    enviar(conexion,'Subject: muestra script en python')
    enviar(conexion,'From:',host)
    enviar(conexion,'To: ',user)
    enviar(conexion,'')
    enviar(conexion,'muestra en python')
    enviar(conexion,'cualquier cosa como mensaje......')
    enviar(conexion,'es un ejemplo......')
    enviar(conexion,'')
    enviar(conexion,'.')
    recibir(conexion)
    enviar(conexion,'quit')