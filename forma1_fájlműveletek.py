import io

""" fajl=open("F1-2024dec.csv",encoding="utf-8")

#fajl_tartalom=fajl.read()
#fajl_tartalom1=fajl.read(111) + "már elfogyott"

#print(fajl_tartalom)
#print(f"\n\n{fajl_tartalom1}")

fajl_tartalom2= []
fajl_tartalom2=fajl.readlines()

print(len(fajl_tartalom2)) """
""" try:
    with open("F1-2024dec-hibás.csv",encoding="utf-8") as fajl:
        pass
except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

print("Itt av éger") """

verseny_adatok = []

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        
        for sor in fajl:
            verseny_adatok.append(sor)

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

#print(verseny_adatok)

    """
    1. Sorozatszámítás/összegzés
    2. Kiválasztás
    3. Megszámolás
    4. Eldöntés 1
        Eldöntés 2
    5.Maximum/minimum kiválasztás
    6. Keresés (lineáris)
    
    7. Szétválogatás
    8. Kiválogatás (külön, helyben)
    9. Unió
    10. Metszet
    
    11. Rendezés
        egyszerű cserés
        buborékos
        minimumkiválasztásos
    """
    
# 1. Mennyi a pontszám átlag?
pontszam = 0
db = len(verseny_adatok)-1
for i in range(1, len(verseny_adatok)):
    sor = verseny_adatok[i].split(",")
    pontszam = pontszam+int(sor[1])
print(f"Pontszámok átlaga: {pontszam/db}")

# 2. Mi a bekért versenyző adatai?
pilota = input("Kérek egy pilótát:")
i=1
while (verseny_adatok[i].split(','))[0] != pilota:
    i+=1

print((verseny_adatok[i]).strip())

# 3. Hány versenyző teljesített 300 pont felett?
db300f=0
for i in range(1,len(verseny_adatok)):
    if int(((verseny_adatok[i]).split(','))[1]) > 300 :
        db300f+=1
print(f"A 300 pont felett teljesítő pilóták száma: {db300f}")

# 4.x Van-e 0 pomtos versenyző?
i=1
hossz=len(verseny_adatok)-1
while i<=hossz and int(verseny_adatok[i].split(',')[1]) != 0 :
    i+=1
if i<=hossz:
    print("Van 0 pontos versenyző!✔")
else:
    print("Nincs 0 pontos versenyző!😊")
    
# 4.y Mindenki szerzett-e már pontot?
i=1

while i<=hossz and int(verseny_adatok[i].split(',')[1]) > 0 :
    i+=1
if i>hossz:
    print("Mindenki szerzett pontot!✔")
else:
    print("Nem mindenki szerzett pontot!😢")

# 5. Ki vezeti a szezont?
maxi=1

max=int((verseny_adatok[maxi].split(','))[1])

for i in range(2,len(verseny_adatok)):
    if max<int((verseny_adatok[i].split(','))[1]):
        max=int((verseny_adatok[i].split(','))[1])
        maxi=i
        
print(f"{(verseny_adatok[maxi].split(','))[0]} vezeti a mezőnyt!")

#6.

#7. Kik a Mercedes pilótái?
db=0
mercisek=[]
for i in range(1,len(verseny_adatok)):
    if verseny_adatok[i].split(',')[2].strip() == "Mercedes":
        mercisek.append(verseny_adatok[i].split(',')[2].strip())
        db+=1
print("A Mercédesz pilótái",mercisek)