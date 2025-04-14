def main():
    a = 5 #basic int stuff
    b = 6.83443 #basic float stuff
    c = True #basic booleans stuff
    s = "basic string stuff"
    
    # print("zmienna a ma wartosc:", a)
    # print("zmienna b ma wartosc:", b)
    # print(f"zmienna a ma wartosc:{a} a zmienna c ma wartosc {c}")

    # print("podaj piersze slowo")
    # w1 = input()
    # print("twoje slowo: ",w1)
    
    
    # w2 = input("Podaj jakies inne slowo: ")
    # print("drugie slowo: ",w2 )
    
    # h = int(input("podaj swoj wiek"))
    # print(f"masz {h} lat")
    
    f = input("True czy False")
    if f == "True":
        print("Prawda")
    elif f == "False":
        print("Fałsz")
    else: raise Exception("Błędne dane")
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()