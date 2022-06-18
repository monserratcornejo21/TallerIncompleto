from distutils.log import error
import socket
ip_origen= '0.0.0.0'                    # 0.0.0.0 es para cualquier origen
puerto_escucha=1234         # puerto a usar, en este caso 1234
con_remota=socket.AF_INET       # Conexión usando IP 
con_tcp=socket.SOCK_STREAM      # Conexión con TCP, para UDP seria     
               

with socket.socket(con_remota,con_tcp) as con:
    con.bind((ip_origen,puerto_escucha))
    con.listen()
    print('Esperando')
    enlace,x= con.accept()
    with enlace as e:
        datos = e.recv(15)
        print('received {!r}'.format(datos))
    # 
    # enlace.close
