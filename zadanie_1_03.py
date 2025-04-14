def main():
    print("Układ równań:")
    print(f"ax + by = c")
    print(f"dx + ey = f")
    
    a = float(input("Podaj współczynnik a równania: "))
    print("Układ równań:")
    print(f"{a}x + by = c")
    print(f"dx + ey = f")
    
    b = float(input("Podaj współczynnik b równania: "))
    print("Układ równań:")
    print(f"{a}x + {b}y = c")
    print(f"dx + ey = f")
    
    c = float(input("Podaj współczynnik c równania: "))
    print("Układ równań:")
    print(f"{a}x + {b}y = {c}")
    print(f"dx + ey = f")
    
    d = float(input("Podaj współczynnik d równania: "))
    print("Układ równań:")
    print(f"{a}x + {b}y = {c}")
    print(f"{d}x + ey = f")
    
    e = float(input("Podaj współczynnik e równania: "))
    print("Układ równań:")
    print(f"{a}x + {b}y = {c}")
    print(f"{d}x + {e}y = f")
    
    f = float(input("Podaj współczynnik f równania: "))
    print("Układ równań:")
    print(f"{a}x + {b}y = {c}")
    print(f"{d}x + {e}y = {f}")
    
    w0 = a*e - d*b
    wx = c*e - f*b
    wy = a*f - d*c
    
    if w0 == 0:
        if wx == 0 and wy == 0:
            print("Układ równań jest nieoznaczony")
        else: print("Układ równań jest sprzeczny")
    else: 
        x = wx/w0
        y = wy/w0
        print(f"Rozwiązaniem układu jest jest x = {x} oraz y = {y}.")
    
if __name__ == "__main__":
    main()