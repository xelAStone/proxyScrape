#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import os
from io import open
import time
import sys
import time
print(sys.platform)
print('ESpera un momento ......')
time.sleep(2)

sitio='https://free-proxy-list.net/'
def respuesta():
	res=requests.get(sitio)
	sp=BeautifulSoup(res.content,'lxml')
	fd=sp.find_all("div",{'class':"table-responsive fpl-list"})
	for i in fd:
		et=i.find_all('td')
		print(et)
	for x in et:
		for i in x:
			print(i)

def rasp():
	res=requests.get(sitio)
	sp=BeautifulSoup(res.content,'lxml')
	fd=sp.find_all("div",{'class':"modal-body"})
	print(fd)
	for y in fd:
		variable=y.find('textarea')
		#print(y)
		num=str(variable)
		abrir=open('proxies.txt','a')
		abrir.write(num)
		abrir.close()
		print('Se han guardado los proxies')
if __name__=='__main__':
	print('a para checar los proxys mas recientes\nb para guardarlos')
	opcion=input('introduce la opcion :')
	if opcion == 'a':
		respuesta()
	elif opcion =='b':
		rasp()
	elif opcion =='':
		print('finalizo el programa')
