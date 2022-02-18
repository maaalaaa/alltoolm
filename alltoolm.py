import os, wget
import sys
import time
import requests
os.system('clear')
os.system('rm -rf shk.txt')
os.system('id -u > shk.txt')
uidd = open('shk.txt', 'r')
for j in uidd:
    sp = j.split()

print("\033[1;92m ")
logo='''

	    __  __       _
|  \/  | __ _| | __ _ _ __ ___
| |\/| |/ _` | |/ _` | '_ ` _ \
| |  | | (_| | | (_| | | | | | |
|_|  |_|\__,_|_|\__,_|_| |_| |_|

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;97m
  Author   : Maaalaaam.
  Chanal Tlegram : @dec_tool
  Telegram : @mala_bek4s
  Nrx:10$
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 = Checker Facbook ID V1 
2 = Checker Facbook ID V2
3 = Checker Facbook ID V3
4 = Checker Facbook Number V1 
5 = Checker Facbook Number V2
6 = Checker Facbook Number V3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
print(logo)
def dwbara():
        chs=raw_input("halbzhera : ")
        if chs=='1':
                wget.download("https://raw.githubusercontent.com/maaalaaa/fbidd/main/fbidd.py")
                os.system("python2 fbidd.py")
        elif chs=='2':
                wget.download("https://raw.githubusercontent.com/maaalaaa/fbiiii/main/fbiiii.py")
                os.system("python2 fbiiii.py")
        elif chs=='3':
                wget.download("https://raw.githubusercontent.com/maaalaaa/idfbm/main/idfbm.py")
                os.system("python2 idfbm.py")
        elif chs=='4':
                wget.download("https://raw.githubusercontent.com/maaalaaa/fbnumber/main/fbnumber.py")
                os.system("python2 fbnumber.py")      
        elif chs=='5':
                wget.download("https://raw.githubusercontent.com/maaalaaa/fbbb/main/fbbb.py")
                os.system("python2 fbbb.py")  
        elif chs=='6':
                wget.download("https://raw.githubusercontent.com/maaalaaa/fbv3/main/fbv3.py")
                os.system("python2 fbv3.py")    
        else:
                print(" Aw zhmaray Tya nya !")
                dwbara()
dwbara()
