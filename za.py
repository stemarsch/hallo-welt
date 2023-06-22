def addiere_zahlen(a, b):
    summe = a + b
    return summe

# Benutzereingaben erhalten
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Zahlen addieren
ergebnis = addiere_zahlen(zahl1, zahl2)

# Ergebnis ausgeben
print("Die Summe ist:", ergebnis)
