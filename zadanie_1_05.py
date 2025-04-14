def main():
    liczba_graczy = int(input("Podaj liczbę graczy: "))
    if liczba_graczy < 2: raise ValueError("To za mało graczy żeby pograć.")
    talie = int(input("Podaj liczbę talii jaką masz: "))
    if talie < 1: raise ValueError("Nie da się grać w makao bez talii kart!")
    
    karty = talie*52
    potrzebne_karty = liczba_graczy*5 + 1
    potrzebne_talie = int((potrzebne_karty-1)/52) + 1
    print(f"By wszyscy gracze mogli zagrać potrzeba {potrzebne_talie} talii.")
    if talie >= potrzebne_talie:
        print("Ilość talii jaką masz wystarczy by zagrać!")
        mozliwi_gracze = int((karty-1)/5)
        print(f"Maksymalnie możesz zagrać w {mozliwi_gracze} osoby w makao (wliczajac w to ciebie).")
    else: print(f"Potrzeba ci {potrzebne_talie-talie} dodatkowych talii.")
    
    
    
if __name__ == "__main__":
    main()