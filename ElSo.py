import random
hlista=[]
for i in range(100):
    szam=random.randint(10,99)
    hlista.append(szam)
#Ellenőrzés
print(hlista)

#Egyszám játék
jatek_szam=0
nem_talaltDB=0

kitalalando_szam=hlista[random.randint(0,len(hlista))] #0-tól kezdi egyébként a randomgenerálást
