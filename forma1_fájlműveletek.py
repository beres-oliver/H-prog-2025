import io

""" fajl=open("F1-2024dec.csv",encoding="utf-8")

#fajl_tartalom=fajl.read()
#fajl_tartalom1=fajl.read(111) + "már elfogyott"

#print(fajl_tartalom)
#print(f"\n\n{fajl_tartalom1}")

fajl_tartalom2= []
fajl_tartalom2=fajl.readlines()

print(len(fajl_tartalom2)) """
try:
    with open("F1-2024dec-hibás.csv",encoding="utf-8") as fajl:
        pass
except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

print("Itt av éger")