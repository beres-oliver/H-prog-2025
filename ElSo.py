import random
hlista=[]
while len(hlista)<40:
    szam=random.randint(10,99)
    if szam not in hlista:
     hlista.append(szam)
#Ellenőrzés
print(hlista)
print(len(hlista))
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
    tipp=input("Tippelj egy egész számot(Kilépés az X betűvel): ").strip()
    if (tipp.isdecimal()):
        tipp=int(tipp)
    else:
        if tipp=='x' or tipp=='X':
            exit()
        print("Egész számmal játssz!")
        continue

    while tipp!=kitalalando_szam:
        print("Nem talált!")
        tipp=input("Tippelj egy egész számot(Kilépés az X betűvel): ").strip()
        if (tipp.isdecimal()):
            tipp=int(tipp)
            if tipp>kitalalando_szam:
                print("Kisebbet tippelj!")
            elif tipp<kitalalando_szam:
                print("Nagyobbat tippelj!")
        else:
            if tipp=='x' or tipp=='X':
                exit()
            print("Egész számmal játssz")
            continue
    
    print("Eltaláltad!")
    jatek_szam+=1

    akarsze=input("Akarsz még játszani (I/N): ")

    if akarsze=='N' or akarsze=='n':
        akare=False