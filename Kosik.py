Ovocie = ("jablko", "hruska", "banan")
Zelenina = ("rajcina")
Zviera = ("pes", "macka")

Kosicek = ("jablko", "hruska", "rajcina", "banan", "pes", "macka")

for i in Kosicek:
    if i in Ovocie:
     print(f"{i} je ovocie")
    elif i in Zelenina:
      print(f"{i} je zelenina")
    else:
        print(f"{i} je zviera")

