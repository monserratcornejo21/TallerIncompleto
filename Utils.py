
from cProfile import label
from cgitb import text
from cmath import e
from tkinter import *
from tkinter import ttk
# from tkinter import _ScreenUnits
from tkinter.tix import ROW
from turtle import width
from mysqlx import Row
from Pop3 import IniciarSesion

from numpy import insert


class redes:
        
    def __init__(self,window):
        
        self.login(window)
        # self.wind.title('Gmailnt')
        # self.wind.resizable(0,0)
        # self.wind.eval('tk::PlaceWindow . center')
        # frame = LabelFrame(self.wind)
        # frame.grid(row = 0, column = 0, columnspan = 2, pady = 20)
        # # Label(frame).grid(row = 1, column = 0 )
        # # self.name = Entry(frame)
        # # self.name.focus()
        # # self.name.grid(row = 1, column = 1)
        # self.message = Label(text = '', fg = 'red')
        # self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        # self.tree = ttk.Treeview(height = 10, columns = 2 )
        # self.tree.grid(row = 2, column = 0, columnspan = 2 , padx=15 )
        # self.tree.heading('#0', text = 'Emisor', anchor = CENTER)
        # self.tree.heading('#1', text = 'Mensaje', anchor = CENTER )
        
        # # ttk.Button(frame, text = 'Agregar', command= self.actualizarCorreo ).grid(row = 3, columnspan = 2, sticky = W + E , padx=10 , pady=10)
        # ttk.Button(text = 'Actualizar', command = '').grid(row = 4, column = 0, sticky = W + E ,  padx=10 , pady=(0,15))
        # ttk.Button(text = 'Redactar Correo', command = self.RedaccionCorreo).grid(row = 4, column = 1, sticky = W + E , padx=10 , pady=(0,15))
    
    
    def RedaccionCorreo(self):
        self2=Tk()
        self2.resizable(0,0)
        self2.title('Redaccion Correo')
        self2.eval('tk::PlaceWindow . center')
        
        frame1 = LabelFrame(self2)
        Label(frame1,text='From'+'   dann@gmail.com').grid(row = 1, column = 0 , padx=(0,15))
        frame1.grid(row = 0, column = 0, columnspan = 2 , pady=5 , padx=(5) , sticky=W)
        
        frame2 = LabelFrame(self2)
        frame2.grid(row = 1, column = 0, columnspan = 2 , pady=5 , padx=5 , sticky=W+E)
        Label(frame2,text='To').grid(row = 1, column = 0 )
        self2.To = Entry(frame2,width=104)
        self2.To.focus()
        self2.To.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        frame3 = LabelFrame(self2)
        frame3.grid(row = 2, column = 0, columnspan = 2, pady=5 , padx=5 , sticky=W+E)
        Label(frame3,text='Subject').grid(row = 1, column = 0 )
        self2.Subject = Entry(frame3,width=100)
        self2.Subject.grid(row = 1, column = 1 , padx=15 , pady=5 ,sticky=W+E)
        
        frame4 = LabelFrame(self2)
        frame4.grid(row = 3, column = 0, columnspan = 2, pady = 5 , sticky=W+E , padx=5)
        Label(frame4).grid(row = 1, column = 0 )
        self2.Messaje = Entry(frame4 ,width=110)
        self2.Messaje.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        ttk.Button(self2,text = 'Descartar', command = self2.destroy).grid(row = 4, column = 0, sticky = W + E , padx=10 , pady=(8,8))
        ttk.Button(self2,text = 'Enviar', command = '').grid(row = 4, column = 1, sticky = W + E ,  padx=10 , pady=(8,8))   
             
        
    def login(self1,self):
        
        self.title('Iniciar Sesion')
        self.eval('tk::PlaceWindow . center')
        frame = LabelFrame(self)
        frame.grid(row = 0, column = 0, columnspan = 2 , pady=5 , padx=5 , sticky=W+E)
        Label(frame,text='Correo').grid(row = 1, column = 0 )
        self.Mail = Entry(frame,width=35)
        self.Mail.focus()
        self.Mail.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        frame2 = LabelFrame(self)
        frame2.grid(row = 1, column = 0, columnspan = 2 , pady=5 , padx=5 , sticky=W+E)
        Label(frame2,text='Pass').grid(row = 1, column = 0 )
        self.Pass = Entry(frame2,width=37)
        self.Pass.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
    
        ttk.Button(self,text = 'Entrar', command ='').grid(row = 4, column = 0, columnspan=5,sticky = W + E , padx=10 , pady=(8,8))
        
        
        
    
    def actualizarCorreo(self):
        self.tree.insert('', 0 , text='Eo',values=self.name.get())
        
    def d(self):
        self.tree.insert('', 0 , text='Eo',values=self.name.get())
    
def enviar(conexion,men):
    msg = men + '\n'
    conexion.send(msg.encode())

def recibir(conexion,num:int):
    msg = conexion.recv(1024)
    if (num==1):
        return msg
    else:
        print(msg.decode())
    
