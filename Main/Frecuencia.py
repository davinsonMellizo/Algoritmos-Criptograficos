#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata
import sys
import codecs
import os
import io
import os.path as path

class Frecuencia:
    def __init__(self):
        self.__alfabeto = []
        self.__frecuencia = [] 
        self.__generar_alfabeto()

    def __generar_alfabeto(self):
        k=0
        archivo = open("alfabeto.txt", mode="r")
        for caracter in archivo.read():
            self.__alfabeto.append(caracter)
            self.__frecuencia.append([0,k])
            k=k+1
        archivo.close()

    def obtenerFrecuencia(self): 
        h=True
        archivo = open(sys.argv[2], mode="r",encoding="ISO-8859-1")
        for caracter in archivo.read():
            posCaracter=self.__alfabeto.index(caracter)
            self.__frecuencia[posCaracter][0]+=1
        archivo.close()
        self.__frecuencia.sort()
        self.obtenerClave()
    def obtenerClave(self):
        posmaximasFrecuencias=[]       
        for i in range(10):
            posmaximasFrecuencias.append(self.__frecuencia[38-i][1])
        posLetrasMaxFrecuencia=[0,4]
        aux=0
        maximo=0
        for i in [0,2]:

            for j in range(9):
                k=0
                kprima=-1
                posMaximo=posmaximasFrecuencias[0]
                posAnterior=posmaximasFrecuencias[j+1]
                if posMaximo>=posLetrasMaxFrecuencia[i+1]:
                    k=posMaximo-posLetrasMaxFrecuencia[i+1]
                else:
                    k=39-posLetrasMaxFrecuencia[i+1]+posMaximo
                if posAnterior>=posLetrasMaxFrecuencia[i]:
                    kprima=posAnterior-posLetrasMaxFrecuencia[i]
                else:
                    kprima=39-posLetrasMaxFrecuencia[i]+posAnterior
                if k!=kprima:

                    if posMaximo>=posLetrasMaxFrecuencia[i]:
                        k=posMaximo-posLetrasMaxFrecuencia[i]
                        
                    else:
                        k=39-posLetrasMaxFrecuencia[i]+posMaximo
                    if posAnterior>=posLetrasMaxFrecuencia[i+1]:
                        kprima=posAnterior-posLetrasMaxFrecuencia[i+1]
                        
                    else:
                        kprima=39+posAnterior-posLetrasMaxFrecuencia[i+1]
                if k==kprima:
                    self.descifrar(-k)
                    
                    print("esta es la clave------  ",k)
                    break
            if k==kprima:
                break
  

    def descifrar(self,key): # formula [Cesar = (LETRA + KEY) % TAM_ALFABETO]
        archivo = open(sys.argv[2], mode="r",encoding="ISO-8859-1")
        if path.exists("Resultado.DEC"):
            os.remove("Resultado.DEC")
        f = open("Resultado.DEC",'w',encoding="ISO-8859-1")
        mensajeCifrado=""
        for caracter in archivo.read():
            posCaracter = self.__alfabeto.index(caracter)
            modulo = (posCaracter+key)%len(self.__alfabeto)
            cifra=self.__alfabeto[modulo]
            mensajeCifrado=mensajeCifrado+cifra
        f.write(mensajeCifrado)
        archivo.close() 
        f.close()
     


        
        
        
        