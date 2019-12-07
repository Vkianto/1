import random
luku=0
numero=1
while luku!=numero:
    luku=random.randint(0,20)
    numero=int(input("Arvaa oikea luku: "))
    if luku==numero:print("Oikea vastaus!")
    if luku==numero:break
    elif numero>20:print("Liian suuri luku, vain max 20!")
    elif numero<0:print("Liian pieni luku, vain 0-20!")
    else: print("Väärin, yritä uudestaan!")
