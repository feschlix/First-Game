# -*- coding: cp1252

#Zufallsgenerator
import random
random.seed()

#Werte und Berechnung
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b

#Ausgabe
print("Die Aufgabe: ", a, "+", b)
print("Bitte Ergebnis eingeben:")

#Eingabe
z = input()
zahl = int(z)

if zahl == c:
    print("Bravo, richtige Antwort!")

else:
    print("Schade, falsche Antwort...")
    print("Die richtige Antwort wäre: ", c)