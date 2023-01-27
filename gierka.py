import random

print("Witaj w zgadywajce :) Naciśnij ENTER aby kontynuować")

contin = input()

print("Zasady: Program losuje jedną liczbę z zakresu od 1 do 1000. "
      "Twoim zadaniem jest odgadnięcie co to za liczba w jak najmniejszej ilości kroków")

print("Naciśnij ENTER aby przejść dalej")
contin = input()

i = 0
i = int(i)

print("Trwa losowanie liczby...")

losowa = random.randint(1,1000)

print("Liczba została wylosowana")

print("Podaj liczbę:")
x = input()
x = int(x)

while losowa != x:
    if x > losowa:
        i += 1
        print("Twoja liczba jest za duża!")
        print("Podaj liczbę:")
        x = input()
        x = int(x)
    else:
        i += 1
        print("Twoja liczba jest za mała!")
        print("Podaj liczbę:")
        x = input()
        x = int(x)

if losowa == x:
    i += 1
    print("Udało się :)")
    print("Szukana liczba to: ")
    print(losowa)
    print("Ilość prób: ")
    print(i)

print("Koniec")