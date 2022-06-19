import socket
from RecEnv import enviar,recibir 

host = "ayredes.ddns.net"
port = 110
ipv4 = socket.AF_INET
tcp  = socket.SOCK_STREAM
conexion = socket.socket(ipv4, tcp)
conexion.connect((host, port))
recibir(conexion)

def ListarCorreos(user, password):
    
    IniciarSesion(user,password)
    enviar(conexion,"LIST\n")
    return recibir(conexion,1)

def IniciarSesion(user, password):
    
    enviar(conexion,"USER {}\n".format(user))
    recibir(conexion)
    
    enviar(conexion,"PASS {}\n".format(password))
    recibir(conexion)

def Funciones(opt:int,id):
    
    if(opt==2):
        print('delete')
    elif(opt==1):
        print('examinar')
    else:
        SalirDelPop() 
    
def SalirDelPop():
    
    enviar(conexion,"QUIT\n")
    return(recibir(conexion,1),"ADIOS.")