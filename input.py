#kerjunk be 0 vegjeleig szamokat es irassuk ki a osszeguket
# osszeg=0

# while True:
#     be_szam=int(input("Kérek egy szamot: "))
#     if be_szam!=0:
#         osszeg=osszeg+be_szam
#     else:
#         break

# print(f"Szamok osszege: {osszeg}")

osszeg=0

be_szam=int(input("kérem a szamot:" ))
while be_szam!="":
    osszeg+=int(be_szam)
    be_szam=input("kérem a számot: ")

print(f"Az összeguk: {osszeg}")


#kerjel be egy szamot es 0tol eddig a paros szamokat irasd ki
hatar=int(input("Kérek egy szamot: "))
szam1=0
while szam1!=hatar+1:
    if szam1%2==0:
        print(szam1)
    szam1+=1


