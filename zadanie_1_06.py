def main():
    n = int(input("Ile ludzi jest na dole? "))
    if n < 0: raise ValueError("Błędne dane - ludzi nie może być mniej niż 0.")
    m = int(input("Ile ludzi jest na górze? "))
    if m < 0: raise ValueError("Błędne dane - ludzi nie może być mniej niż 0.")
    
    kursy_wgore = n/8
    if int(kursy_wgore) != kursy_wgore:
        kursy_wgore = int(kursy_wgore) + 1
    kursy_wdol = m/8
    if int(kursy_wdol) != kursy_wdol:
        kursy_wdol = int(kursy_wdol) + 1
    
    if kursy_wgore > kursy_wdol:
        print(f"Winda musi zrobić {kursy_wgore*2 - 1} kursów.")
    else:
        print(f"Winda musi zrobić {kursy_wdol*2} kursów")
    
    
if __name__ == "__main__":
    main()