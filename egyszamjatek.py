import random
hlista=[]
while len(hlista)<40:
    szam=random.randint(10,99)
    if szam not in hlista:
     hlista.append(szam)
#Ellenőrzés
print(hlista)
#Egyszám játék
jatek_szam=0
nem_talaltDB=0

kitalalando_szam=hlista[random.randint(0,len(hlista))]
#játék
""" 
tipp_szám=int(input("Tippelj egy egész számot: "))

while tipp_szám!=kitalalando_szam:
    print("Nem talált!")
    tipp_szám=int(input("Tippelj újat: "))
    
print("Eltaláltad!")

akarsze=input("Akarsz még játszani (I/N): ")

if akarsze=='I':
    #???
    pass
else:
    exit() """

#játék újrajátszható
akare=True
while akare:
    nem_talaltDB=0
    kitalalando_szam=hlista[random.randint(0,len(hlista))]
    tipp=input("Tippelj egy egész számot(Kilépés az X betűvel): ").strip()
    if (tipp.isdecimal()):
        tipp=int(tipp)
    else:
        if tipp=='x' or tipp=='X':
            print("Ennyiszer játszotta a játékot:",jatek_szam)
            print("Ennyi rossz probálkozása volt:",nem_talaltDB)
            exit()
        print("Egész számmal játssz!")
        continue
    if nem_talaltDB!=0:
        print("Nem talált!")
    while tipp!=kitalalando_szam:
        if nem_talaltDB==0:
            nem_talaltDB+=1
        tipp=input("Tippelj egy egész számot(Kilépés az X betűvel): ").strip()
        if (tipp.isdecimal()):
            tipp=int(tipp)
            if tipp>kitalalando_szam:
                nem_talaltDB+=1
                print("Kisebbet tippelj!")
            elif tipp<kitalalando_szam:
                nem_talaltDB+=1
                print("Nagyobbat tippelj!")
        else:
            if tipp=='x' or tipp=='X':
                exit()
            print("Egész számmal játssz")
            continue
            
    print("Eltaláltad!")
    jatek_szam+=1
    print("Ennyiszer játszotta a játékot:",jatek_szam)
    print("Ennyi rossz probálkozása volt:",nem_talaltDB)

    akarsze=input("Akarsz még játszani (I/N): ")

    if akarsze=='N' or akarsze=='n':
        akare=False