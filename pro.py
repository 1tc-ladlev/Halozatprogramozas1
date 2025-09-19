print ("Szia", end=" ")
print ("Tibi")
print ("Szia", "Tóth", "Karcsi", "!", sep="")
print ("Szia Tóth Karcsi!")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!") 

#ADATTIPUSOK
# int()
# float()
# str()
# bool()
# list()
# set()
#tuple
print()
print(int("5"))
print(float(5))
print(str(5.0))
print(type(str(5.0)))
print(bool(-1))
print(["hetfő", "kedd", "szerda"])
napok = ["hetfő","kedd","szerda"]
print(f"Napok: {napok}")
nevek = ["Tibi","Sanyi","Tibi"]
print(f"Nevek: {set(nevek)}")
print(tuple([1,2,3]))

#HF: git parancsok

#
#
# git clone - https://github.com/1tc-ladlev/Halozatprogramozas1.git  - a githubról klónozol
# git init – adott mappa verziókövetésének indítása
# git config --global user.name "felhasználóneved" – felhasználónév beállítása
# git config --global user.email "emailed" – email beállítása
# git status – repository állapotának lekérdezése
# git add fajl.txt – fájlok stage-elése
# git commit -m "üzenet" – stage-elt változtatások végleges mentése
# git push – commitok feltöltése a távoli repóba
#
#