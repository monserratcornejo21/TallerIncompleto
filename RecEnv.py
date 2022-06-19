from ast import Num


def enviar(conexion,men):
    msg = men + '\n'
    conexion.send(msg.encode())

def recibir(conexion,num:int):
    msg = conexion.recv(1024)
    if (num==1):
        return msg
    else:
        print(msg.decode())