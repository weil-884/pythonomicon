def main():
    
   waga = int(input("Podaj swoją wagę w kilogramach: "))
   if waga <= 0: raise ValueError("Twoja waga musi być większa od 0kg")
   
   wzrost_cm = int(input("Podaj swój wzrost w centymetrach: "))
   if wzrost_cm <= 0: raise ValueError("Twój wzrost musi być większy od 0cm")
   wzrost_m = wzrost_cm/100

   bmi = waga/(wzrost_m*wzrost_m)
   
   if bmi <= 18.5: print("masz niedowagę") 
   elif bmi <= 25: print("twoja waga jest prawidłowa")
   elif bmi <= 30: print("masz nadwagę")
   else:           print("jestes otyły")
   
if __name__ == "__main__":
    main()