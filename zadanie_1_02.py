def main():
    k = 0
    #P = A/KW
    gender = input("Podaj swoją płeć: ")
    if gender == "mężczyzna":
        k = 0.7
    elif gender == "kobieta":
        k = 0.6
    else: raise ValueError("Są tylko 2 płcie lol")
    
    w = int(input("Podaj masę ciała w kg: "))
    if w <= 0: raise ValueError("ta wartość nie może być ujemna")
    
    a = int(input("Podaj ilość wypitego alkoholu w ml: "))
    a = (a/12.5)*10
    if a < 0: raise ValueError("ta wartość nie może być ujemna")
    
    p = a/(k*w)
    
    if p <= 0.2: print("Jesteś trzeźwy! (kinda lame ngl)")
    elif p <= 5: print("Nie jesteś trzeźwy i nie możesz prowadzić pojazdu")
    else:        print("Jesteś w stanie zagrożenia życia (no chyba że jesteś polakiem )")
    
        
    
if __name__ == "__main__":
    main()