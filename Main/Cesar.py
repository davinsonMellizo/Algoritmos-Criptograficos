#!/usr/bin/env python
# -*- coding: latin1 -*-

import unicodedata
import sys
import codecs
import os
import shutil
import os.path as path
import time



class CifradoCesar:
    def __init__(self, key):
        self.__key = key
        self.__alfabeto = []

        self.__generar_alfabeto()
    def __generar_alfabeto(self):
        archivo = open("alfabeto.txt", mode="r")
        for caracter in archivo.read():
            self.__alfabeto.append(caracter)
        archivo.close()
        insFinal=time.time()
           

        
    def cifrar(self): # formula [Cesar = (LETRA + KEY) % TAM_ALFABETO]
        archivo =open(sys.argv[3],"r",encoding="ISO-8859-1")        
        f = open("Resultado.CIF",'w',encoding="ISO-8859-1")
        tamAlfa=len(self.__alfabeto)
        mensajeCifrado=""
        for caracter1 in archivo.read():
            posCaracter = self.__alfabeto.index(caracter1)
            modulo = (posCaracter+self.__key)%tamAlfa
            cifra=self.__alfabeto[modulo]
            mensajeCifrado=mensajeCifrado+cifra
        f.write(mensajeCifrado)
        archivo.close() 
        f.close()
        
    def descifrar(self): # formula [Cesar = (LETRA + KEY) % TAM_ALFABETO]
        archivo = open(sys.argv[3], "r",encoding="ISO-8859-1")
        f = open("Resultado.DEC",'w',encoding="ISO-8859-1")
        tamAlfa=len(self.__alfabeto)
        mensajeDescifrado=""
        for caracter in archivo.read():
            posCaracter = self.__alfabeto.index(caracter)
            modulo = (posCaracter-self.__key)%tamAlfa
            cifra=self.__alfabeto[modulo]
            mensajeDescifrado=mensajeDescifrado+cifra
        f.write(mensajeDescifrado)
        archivo.close() 
        f.close()
