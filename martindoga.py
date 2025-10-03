lista=[1,2,4,5,]

osszeg=0
for szam in lista:
    osszeg=osszeg+szam

print(f"A számok összege: {osszeg} ")
print(len(lista))


p_szamok=[]

for szam in lista:
    if szam%2==0:
        p_szamok.append(szam)
print(f"A páros számok: {p_szamok}")

nevek=[]

while True:
    nev=input("Kérem a keresztnevet: ") 
    if nev in nevek: 
        break
    nevek.append(nev)
print(nevek)


