print("Wybierz: kamien, papier, nozyczki")
gracz2_wynik = 0
gracz1_wynik = 0
while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracza1 = input("Gracz1 podaj swój wybór: ")
    wybor_gracza2 = input("Gracz2 podaj swój wybór: ")
    w1 = 'Wygrał gracz1! '
    w2 = "Wygrał gracz2! "
    if wybor_gracza1 == 'papier' and wybor_gracza2 == "kamien":
            print(w1)
            gracz1_wynik += 1
    elif wybor_gracza1 == 'nozyczki' and wybor_gracza2 == "papier":
        print(w1)
        gracz1_wynik += 1
    elif wybor_gracza1 == 'kamien' and wybor_gracza2 == 'nozyczki':
        print(w1)
        gracz1_wynik += 1
    elif wybor_gracza1 == wybor_gracza2:
        print('Remis!')
    else: print(w2)
    gracz2_wynik += 1



