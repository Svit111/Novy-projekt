Ovocie = ["jablko", "hruska", "banan", "hrozno"]
Zelenina = ["rajcina","melon"]
Zviera = ["pes", "macka", "zajac"]
kosik = []

while True:
   print("Kosik veci")
   vstup = input()
   if vstup == "uz nic" or vstup == "koniec":
      break
   else:
      kosik.append(vstup)

a = "Hello World!"
print(a)

for i in kosik:
    if i in Ovocie:
     print(f"{i} je ovocie")
    elif i in Zelenina:
      print(f"{i} je zelenina")
    else:
        print(f"{i} nepoznam")

# pouzi slovnik a dvojcu, kazda polozka bude par nazov a cena, [("mlieko", 2), "mlieko", 2)]
# pridaj ceny veciam, spocitaj ceny na konci

