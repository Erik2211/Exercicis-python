def dem_valors():
    while True:
        try:
            n = int(input("Dime un numero del 1 al 10: "))
            if n < 1 or n > 10:
                print("Debe ser entre el 1 y el 10")
            else:
                return n
                break
        except ValueError:
            print("Deben ser numeros enteros")
                
         


if __name__=="__dem_valors":
    dem_valors()