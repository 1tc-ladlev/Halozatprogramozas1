#kerjunk be szamokat és meg az összegüket!

# while bennmaradasi feltetel:
#     ciklus mag
# 1 0 végjelig
# 2 Enter végjelig HF: ha entert ut legyen vege és irja ki az összeget
osszeg=0
szam=1
while szam !=0:
    szam=int(input("kérek egy szamot: "))
    osszeg+=szam

print(osszeg)


