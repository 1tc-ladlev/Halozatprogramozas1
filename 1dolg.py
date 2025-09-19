#B csoport

# B.1. Számok darabszáma: 5
# B.2. Páros számok darabszáma: 3
# AB.3. Sávdiagram:
# 2: **
# 4: ****
# 1: *
# 8: ********
# 3: ***

lista=[2,4,1,8,3]

#1
print("Számok darabszáma: ", len(lista))    

# #2
def paros(lista):
    paros_db=0
    for elem in lista:
        if elem%2==0:
            paros_db+=1
    return paros_db

print(f"A lista páros darabszáma: {paros(lista)}")

#3
print("Sávdiagram: ")




