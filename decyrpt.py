from Crypto.Cipher import XOR
import base64
import os
import sys

def decrypt():
        key = 'teste123@'
        cipher = XOR.new(key)
        pathfile = '/download/controlado'
        openfile = open(pathfile,'rb')
        readfile = openfile.read()
        openfile.close()
        encoding = cipher.decrypt(base64.b64decode(readfile))
        os.system('rm ' +pathfile)
        openfile2 = open(pathfile,'wb')
        openfile2.write(encoding)
        openfile2.close()
decrypt()
