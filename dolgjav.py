lista=[2,4,1,8,3]

#A1
#lista összeg
osszeg=0
for szam in lista:
    osszeg+=szam

print(f"osszege: ", osszeg)
print(f"osszege: ", len(lista))

#B1
#darabszam
darab=0
for szam in lista:
    darab+=1

print(f"darabszam: {darab}")
print(f"darabszam: ", len(lista))


#A2
paros_osszeg=0
paros_db=0

for szam in lista:
    if szam%2==0:
        paros_osszeg+=szam
        paros_db+=1

print(f"paros szamok atlaga:  {paros_osszeg / paros_db:.3}")

#B2
#paros szamok darabszama

def paros(lista):
    paros_db=0
    for elem in lista:
        if elem%2==0:
            paros_db+=1
    return paros_db

print(f"A lista páros darabszáma: {paros(lista)}")

#A.2 B.2
parosok=[szam for szam in lista if szam%2==0]
print(f"paros szamok atlaga:  {sum(parosok) /  len(parosok):.3}")
print(f"paros szamok darabszama: {len(parosok)}")


#AB.3 savdiagram
for szam in lista:
    print(szam, "*" * szam)