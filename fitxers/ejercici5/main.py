import menu
import valors
import ej1 
import ej2
import ej3

def main():
    while True:
        menu.menu()
        while True:
            try:
                opc = int(input("Seleccione una opción: "))
                if opc < 1 or opc > 4:
                    print("Seleccione entre 1 o 4")
                break
            except ValueError:
                print("Deben ser numeros enteros")  
        if opc == 4:
            exit() 

        if opc == 1:
            a = valors.dem_valors()
            ej1.ej1(a)
            print("Tabla hecha.")

        if opc == 2:
            a = valors.dem_valors()
            ej2.ej2(a)

        if opc == 3:
            a = valors.dem_valors()
            b = valors.dem_valors()
            ej3.ej3(a,b)

if __name__=="__main__":
    main()
        

