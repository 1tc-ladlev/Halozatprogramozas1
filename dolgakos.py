nevek=["Tibi","Évi", "Sanyi", "Karcsi", "Lili"]
nemek=[1,2,1,1,2]

#hany fiu van?
#fiuk nevei
#hany % fiuk aranya

# for i in range (len(nevek)):
#     print(nevek [i])

#hany fiu van?
fiunevek = []
for i in range(len(nevek)):
    if nemek[i] == 1:
        fiunevek.append(nevek[i])

print(len(fiunevek), "fiu van")

#fiuk nevei
fiunevek = []
for i in range(len(nevek)):
    if nemek[i] == 1:
        fiunevek.append(nevek[i])

print(f"fiuk nevei: {fiunevek}")

#hany % fiuk aranya
print(f"{len(fiunevek) /len(nevek)*100}% a fiuk aranya")