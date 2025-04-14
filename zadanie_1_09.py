def main():
    
    pizza = int(input("Ile placków pizzy chcesz zamowic? "))
    if pizza < 0: raise ValueError("Błedne dane.")
    cola = int(input("Ile butli coli chcesz zamowic? "))
    if cola < 0: raise ValueError("Błedne dane.")
    
    zestaw = min(pizza,cola)
    pizza_solo = pizza-zestaw
    cola_solo = cola - zestaw
    
    if zestaw > 0:
        koszt = zestaw*25.99 + pizza_solo*19.99 + cola_solo*6.99
    else:
        koszt = 5 + pizza_solo*19.99 + cola_solo*6.99
        
    print("Zeby bylo najtaniej musisz zamowic: ")
    print(f"{zestaw} - zestawow")
    print(f"{pizza_solo} - plackow pizzy")
    print(f"{cola_solo} - butelek coli")
    print(f"To bedzie kosztowac {koszt} pln.")

    
if __name__ == "__main__":
    main()