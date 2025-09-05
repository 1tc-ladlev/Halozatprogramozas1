#feladat: negyzet/teglalap kerületenek szamitasa 
def beker(alakzat, oldal):
    """Bekéri az alakzat oldal oldalanak hosszát"""
    oldalhossz = int(input("Kérem a {alakzat} {oldal} oldalának hosszát [cm]: "))
    return oldalhossz

def teglalapKerulete(a, b):
    """kiszamolja az a és b oldal ismereteben a teglalap keruletet.  K= 2*(a+b)"""
    kerulet = 2 * (a + b)
    return kerulet

def kiir(alakzat, kerulet):
    """Kirija az alakzat teruletet"""
    print(f"A {alakzat} kerulete: {kerulet} cm.")

#input
mit = input("[T]églalap vagy [N]égyzet keruletet szamoljam? T|N: ")
if mit.upper() == "N":
    alap = beker("negyzet", "a")
#calculation
    kerulet = teglalapKerulete(alap, alap)
#output
    print(f"A negyzet kerülete: {kerulet} cm")

elif mit.upper() == "T":
    a_oldal = beker("teglalap", "a")
    b_oldal = beker("teglalap", "b")
#calculation
    kerulet = teglalapKerulete(a_oldal, b_oldal)
#output
    print(f"A téglalap kerülete: {kerulet} cm")
else:
    print("Hibás választás. Kilépek!")
