#!/usr/bin/python3
import requests
import os
import random
import time

print('Esta es una herramienta para verificar que proxy esta funcional')
print(time.ctime(),'==> xela-stone')
print('[x]http\n[y]socks4\n[z]socks5')
proto=input('ingresa los valores -> : ')
if proto == 'x':
	proto='http'
if proto == 'y':
	proto='socks4'
if proto == 'z':
	proto='socks5'
ruta=input('Introduce la ruta de los proxys -> : ')
nombre=input('Introduce el nombre del archivo ->: ')

archivo=open(ruta+nombre).readlines()
archivo=[x.rstrip()for x in archivo]
for lineas in archivo:
	proxies={"https":proto+f"://{lineas}"}
	try:
		res=requests.get("https://canihazip.com/s",proxies=proxies,timeout=2)
		if res.text in lineas:
			print('el proxy esta vivo {}'.format(lineas))
			print(lineas,archivo=open('proxys_vivos.txt','a'))
		else:
			print('el proxy esta muerto {}'.format(lineas))
			print(lineas,archivo=open('proxys_muertos.txt','a'))
	except KeyboardInterrupt as y:
		print('finalizado')
		break
	except:
		pass
