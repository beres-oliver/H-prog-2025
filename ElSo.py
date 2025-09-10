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

tipp_szám=int(input("Tippelj egy egész számot: "))

while tipp_szám!=kitalalando_szam:
    print("Nem talált!")
    tipp_szám=int(input("Tippelj újat: "))
    
print("Eltaláltad!")

akarsze=input("Akarsz még játszani (I/N): ")

if ()