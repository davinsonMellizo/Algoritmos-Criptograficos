#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unicodedata
import sys
import codecs
import os
import io
import os.path as path
import base64
from PIL import Image

class Atbash:
    def __init__(self, cod):
        self.__alfabeto = ""
        self.__alfClave = ""
        self.__codificar = cod
        self.__generar_alfabeto()
    def __generar_alfabeto(self):
        if(self.__codificar=="S"):
            archivo = open("alfabeto64.txt", mode="r")
        else:
            archivo = open("alfabeto.txt", mode="r")
        for caracter in archivo.read():
            self.__alfabeto=self.__alfabeto+caracter
            self.__alfClave=caracter +self.__alfClave
        
        archivo.close()
       
    def cifrar(self): 
        archivo = open(sys.argv[3], mode="r", encoding="ISO-8859-1")
        f = open ("Resultado.CIF",'w',encoding="ISO-8859-1")
        mensajeCifrado=""
        texto=archivo.read()
        if(self.__codificar=="S"):
            texto=texto.encode("utf-8")
            texto=base64.b64encode(texto)
            texto=texto.decode("utf-8")

        for caracter in texto:
            posCaracter = self.__alfabeto.find(caracter)
            mensajeCifrado=mensajeCifrado+self.__alfClave[posCaracter]
        f.write(mensajeCifrado)

        archivo.close() 
        f.close()
        
    def descifrar(self): 
        archivo = open(sys.argv[3], mode="r", encoding="ISO-8859-1")
        texto=archivo.read()
        f = open ("Resultado.DEC",'w',encoding="ISO-8859-1")
        mensajeDescifrado=""
        for caracter in texto:
            posCaracter = self.__alfClave.index(caracter)
            mensajeDescifrado=mensajeDescifrado+self.__alfabeto[posCaracter]
        if(self.__codificar=="S"):
            mensajeDescifrado=base64.b64decode(mensajeDescifrado)
            mensajeDescifrado=mensajeDescifrado.decode("utf-8")
        f.write(mensajeDescifrado)
        archivo.close() 
        f.close()

        
        
        