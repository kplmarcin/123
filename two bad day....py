print("Wybierz: kamien, papier, nozyczki")
wybor_gracza1 = input("Gracz1 podaj swój wybór: ")
wybor_gracza2 = input("Gracz2 podaj swój wybór: ")
w1 = 'Wygrał gracz1! '
w2 = "Wygrał gracz2! "
if wybor_gracza1 == 'papier' and wybor_gracza2 == "kamien" or wybor_gracza1 == 'nozyczki' and wybor_gracza2 == "papier"  or wybor_gracza1 == 'kamien' and wybor_gracza2 == 'nozyczki':
    print(w1)
elif wybor_gracza1 == wybor_gracza2:
    print('Remis!')
else: print(w2)


