def main():
   
   a = int(input("Podaj wymiar a: "))
   b = int(input("Podaj wymiar b: "))
   c = int(input("Podaj wymiar c(wysokość): "))
    
   powierzchnia = 2*(a+b)*c
   ROLKA = 2.548
   
   ile_rolek = powierzchnia/ROLKA
   
   if ile_rolek > 400:
      koszt = 100 + (int(ile_rolek)+1)*1.37
   else:
      koszt = (int(ile_rolek)+1)*1.37
   
   print(f"Potrzeba {ile_rolek} rolek")
   print(f"Kosztowac cie to bedzie {koszt} zl")
   
   
    
if __name__ == "__main__":
    main()