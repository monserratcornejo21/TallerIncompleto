# import logging
# import os
# from distutils.log import error
# import random
# from sys import flags
# import traceback
# from curses import window
from time import sleep
from tkinter import *
from Utils import redes
# from turtle import title


if __name__ == '__main__':
    print("Abrir consola pra enviar correo")
    window=Tk()
    redes(window)
    window.mainloop()
