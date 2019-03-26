#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import codecs
from Cesar import CifradoCesar as CF
from Frecuencia import Frecuencia as FR
from polybios import CifradoPolybios as PB
from Atbash import Atbash as AT
import menu
import time
#METO QUE LLAMA LA FUNCION DE CIFRAR CON EL METODO DE CESAR
def cifrarcesar(key):
	insInicial=time.time()
	print("Procesando...")
	print()
	cf = CF(key)
	cf.cifrar()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoCIF()
#METO QUE LLAMA LA FUNCION DE DESCIFRAR CON EL METODO DE CESAR
def descifrarcesar(key):
	insInicial=time.time()
	print("Procesando...")
	print()
	cf = CF(key)
	cf.descifrar()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoDEC()
#METO QUE LLAMA LA FUNCION DE CIFRAR CON EL METODO POLYBIOS
def cifrarpolybios(alfabeto,cod):
	insInicial=time.time()
	print("Procesando...")
	print()
	pb = PB(alfabeto,cod)
	pb.cifrar()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoCIF()
#METO QUE LLAMA LA FUNCION DE DESCIFRAR CON EL METODO DE POLYBIOS
def descifrarpolybios(alfabeto,cod):
	insInicial=time.time()
	print("Procesando...")
	print()
	pb = PB(alfabeto,cod)
	pb.descifrar()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoDEC()
def AnalisisFrecuencia():
	insInicial=time.time()
	print("Procesando...")
	print()
	fr = FR()
	fr.obtenerFrecuencia()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoDEC()
def cifrarAtbash(cod):
	insInicial=time.time()
	print("Procesando...")
	print()
	at = AT(cod)
	at.cifrar()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoCIF()
def descifrarAtbash(cod):
	insInicial=time.time()
	print("Procesando...")
	print()
	at = AT(cod)
	at.descifrar()
	menu.fin()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	menu.resultadoDEC()
def codificar():
	while True:
		cod=input("Desea Codificar en base64? S/N: ")
		if(cod=="S" or cod=="N"):
			break
	return cod
def main():
	mostrarMenu=True
	#SI SOLO SE EJECUTA EL PROGRAMA MUESTRA EL MENU
	if len(sys.argv)<=1:
		menu.algoritmos()
	else:
		#si es igual a dos puede ser una ayuda
		if(len(sys.argv)==2):
			if sys.argv[1]=="-jc" :
				menu.ayudacesar()
				mostrarMenu=False
			if sys.argv[1]=="-pb" :
				menu.ayudapolybios()
				mostrarMenu=False
			if sys.argv[1]=="-af" :
				menu.ayudaFrecuencia()
				mostrarMenu=False
			if sys.argv[1]=="-at" :
				menu.ayudaAtbash()
				mostrarMenu=False
			
		if(len(sys.argv)==3):
			if sys.argv[1]=="-af":
				AnalisisFrecuencia()
				mostrarMenu=False
		#si es igual a 5 puede ser julio cesar o Atbash	
		if (len(sys.argv)==5):
			if sys.argv[1]=="-at" and sys.argv[2]=="-c":
				if(sys.argv[3]=="-N" or sys.argv[3]=="-S" or sys.argv[3]=="-n" or sys.argv[3]=="-s"):
					cod=sys.argv[3]
					cifrarAtbash(cod)
					mostrarMenu=False
			if sys.argv[1]=="-at" and sys.argv[2]=="-d":
				if(sys.argv[3]=="-N" or sys.argv[3]=="-S" or sys.argv[3]=="-n" or sys.argv[3]=="-s"):
					cod=sys.argv[3]
					descifrarAtbash(cod)
					mostrarMenu=False
		#si es igual a 6 puede ser polybios
		if(len(sys.argv)==6):
			if sys.argv[1]=="-jc" and sys.argv[2]=="-c":
				cifrarcesar(int(sys.argv[4]))
				mostrarMenu=False
			if sys.argv[1]=="-jc" and sys.argv[2]=="-d":
				descifrarcesar(int(sys.argv[4]))
				mostrarMenu=False
			if sys.argv[1]=="-pb" and sys.argv[2]=="-c" and sys.argv[3]=="-n":
				if(sys.argv[4]=="-N" or sys.argv[4]=="-S" or sys.argv[4]=="-n" or sys.argv[4]=="-s"):
					cod=sys.argv[4]
					cifrarpolybios("n",cod)
					mostrarMenu=False
			if sys.argv[1]=="-pb" and sys.argv[2]=="-c" and sys.argv[3]=="-l":
				if(sys.argv[4]=="-N" or sys.argv[4]=="-S" or sys.argv[4]=="-n" or sys.argv[4]=="-s"):
					cod=sys.argv[4]
					cifrarpolybios("l",cod)
					mostrarMenu=False
			if sys.argv[1]=="-pb" and sys.argv[2]=="-d" and sys.argv[3]=="-n":
				if(sys.argv[4]=="-N" or sys.argv[4]=="-S" or sys.argv[4]=="-n" or sys.argv[4]=="-s"):
					cod=sys.argv[4]
					descifrarpolybios("n",cod)
					mostrarMenu=False
			if sys.argv[1]=="-pb" and sys.argv[2]=="-d" and sys.argv[3]=="-l":
				if(sys.argv[4]=="-N" or sys.argv[4]=="-S" or sys.argv[4]=="-n" or sys.argv[4]=="-s"):
					cod=sys.argv[4]
					descifrarpolybios("l",cod)
					mostrarMenu=False
		if(mostrarMenu):
			menu.algoritmos()

		
#METODO QUE INICIA EL PROGRAMA		
if __name__ == '__main__':
    main()

    