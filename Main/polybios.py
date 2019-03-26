#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
import os
import os.path as path
import base64
class CifradoPolybios:
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, alfabetoP,cod):
        self.__alfabeto=""
        self.__codificar = cod
        if alfabetoP=="l":
            self.__alfabetoC =  "ABCDEFGHI"
        else:
            self.__alfabetoC =  "123456789"
        self.__generar_alfabeto()
    def __generar_alfabeto(self):
        if(self.__codificar=="S"):
            archivo = open("alfabeto64.txt", mode="r")
        else:
            archivo = open("alfabeto.txt", mode="r")
        for caracter in archivo.read():
            self.__alfabeto=self.__alfabeto+caracter
        archivo.close()
        
    #METODO POLYBIOS PARA CIFRAR
    def cifrar(self): 
        archivo = open(sys.argv[4], mode="r",encoding="ISO-8859-1")
        f = open ("Resultado.CIF",'w',encoding="ISO-8859-1")
        posLetra=0
        mensajeCifrado=""      
        texto=archivo.read()
        if(self.__codificar=="S"):
            texto=texto.encode("utf-8")
            texto=base64.b64encode(texto)
            texto=texto.decode("utf-8")
        for caracter in texto:
        
            posLetra=self.__alfabeto.find(caracter) #OBTIENE LA POSICION DEL CARACTER EN EL ALFABETO
            posHor=posLetra%9 #POSICION DE COLUMNA EN LA MATRIZ
            posVer=int(posLetra/9) #POSICION DE FILA EN LA MATRIZ
            #GUARDAMOS LAS DOS LETRAS
            mensajeCifrado=mensajeCifrado+self.__alfabetoC[posVer]
            mensajeCifrado=mensajeCifrado+self.__alfabetoC[posHor]
        
        f.write(mensajeCifrado)
                
        archivo.close()
        f.close()
        
    #METODO POLYBIOS PARA DESCIFRAR
    def descifrar(self): 
        archivo = open(sys.argv[4], mode="r", encoding="ISO-8859-1")
        f = open ("Resultado.DEC",'w',encoding="ISO-8859-1")
        mensajeDescifrado=""
        while True:
            caracter1=archivo.read(1)
            caracter2=archivo.read(1)
            if not caracter1:
                    break
            posVer=self.__alfabetoC.find(caracter1)#POSICION EN LAS COLUMNAS
            posHor=self.__alfabetoC.find(caracter2)#POSICION EN LAS FILAS
            posEnAlfabeto=posHor+posVer*9 #POSICION EN EL ALFABETO
            #SE GUARDA LA LETRA DESCIFRADA
            mensajeDescifrado=mensajeDescifrado+self.__alfabeto[posEnAlfabeto]
        
        if(self.__codificar=="S"):
            mensajeDescifrado=base64.b64decode(mensajeDescifrado)
            mensajeDescifrado=mensajeDescifrado.decode("utf-8")
        f.write(mensajeDescifrado)
                
        archivo.close()
        f.close()
        
                
        
        
        
        
        