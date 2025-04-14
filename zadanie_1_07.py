def main():
    
    portfel = float(input("Ile masz pieniędzy przy sobie?"))
    if portfel < 0: raise ValueError("Nie możesz mieć ujemnych pieniędzy.")
    
    odleglosc = int(input("Jaka odleglos masz do domu? w pełnych km tzn. 3,7km = 4km, 5,2km = 6km : "))
    if odleglosc < 0: raise ValueError("Nie da się być ujemną odleglosc od domu.")
    if odleglosc == 0: raise ValueError("Przecież już jesteś w takim razie w domu!")
    
    if odleglosc <= 20:
        koszt = 10 + odleglosc*2.5
    else:
        koszt = 60 + (odleglosc-20)*5
    
    if portfel >= koszt:
        print("dasz rade dotrzec do domu")
    elif portfel <= 12.5:
        print("Nie masz pieniedzy na rozpoczecie przejazdu lub na ani jeden kilometr")
    else:
        portfel = portfel - 10
        zasieg = 0
        if portfel >= 50:
            portfel = portfel - 50
            zasieg = int(portfel/5)
            print("Nie dasz rady dotrzec do domu")
            print(f"Możesz przejechac {20+zasieg} km za te pieniadze")
        else:
            zasieg = int(portfel/2.5)
            print("Nie dasz rady dotrzec do domu")
            print(f"Możesz przejechac {zasieg} km za te pieniadze")
        
    
if __name__ == "__main__":
    main()