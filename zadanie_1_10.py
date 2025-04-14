def main():
    
    cena = float(input("Ile kosztuje litr paliwa? "))
    if cena <= 0: raise ValueError("kolezko paliwo nie jest tak tanie!")
    
    spalanie = float(input("Ile twoje auto spala na 100 km?"))
    spalanie_na_km = spalanie/100
    if spalanie < 3 or spalanie > 50:
        raise ValueError("Błędne dane lol")
    
    portfel = int(input("Ile masz pieniedzy? "))
    if portfel < 0: raise ValueError("bro you cant be that broke")
    
    odleglosc = int(input("Ile chcesz przejechac? "))
    if odleglosc < 0: raise ValueError("Błędne dane")
    
    koszt_100km = cena*spalanie
    koszt_1km = cena*spalanie_na_km
    
    zasieg = portfel/koszt_1km
    
    
    
    print(f"Za posiadaną kwotę możesz przejechać {zasieg} km.")
    print(f"Koszt paliwa za 1km to {koszt_1km}")
    
    if zasieg >=odleglosc:
        print("Możesz jechać!")
    else:
        roznica = odleglosc - zasieg
        koszt_roznicy = roznica*koszt_1km
        print(f"Niestety brakuje ci {koszt_roznicy}")
            
if __name__ == "__main__":
    main()