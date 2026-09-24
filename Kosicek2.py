Ovocie = {
    "jablko": 1,
    "banan": 2,
    "hruska": 3
}
Zelenina = {
    "rajcina": 2,
    "melon": 3
}
Zviera = {
    "pes": 10,
    "macka": 20
}

Mnozstvo = {
    "jablko": 5, "banan": 3, "hruska": 4,
    "rajcina": 2, "melon": 1,
    "pes": 1, "macka": 2
}

kosicek = []
cena = 0

while True:
    print("Kosik veci")
    vstup = input()
    if vstup == "uz nic" or vstup == "koniec":
        break
    else:
        if vstup in Mnozstvo:
            if Mnozstvo[vstup] > 0:
                kosicek.append(vstup)
                Mnozstvo[vstup] -= 1  # Odobratie 1 kusu zo skladu
            else:
                print(f"Vypredané!")
        else:
            kosicek.append(vstup)


a = "ooooooooooooooooooooooooooooo"
print(a)

for i in kosicek:
    if i in Ovocie:
        print(f"{i} je ovocie, stoji {Ovocie[i]}")
        cena += Ovocie[i]
    elif i in Zelenina:
        print(f"{i} je zelenina, stoji {Zelenina[i]}")
        cena += Zelenina[i]
    elif i in Zviera:
        print(f"{i} je zviera, stoji {Zviera[i]}")
        cena += Zviera[i]
    else: 
        print(f"{i} nepoznam")

print(f"Cena: {cena}")
