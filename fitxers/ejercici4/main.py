import ejercici1 as ej1
import ejercici2 as ej2
import ejercici3 as ej3
# Modifica els programes anteriors per a que el programa tinga una funció main() on es realitze el que
# es demane

while True:
    print("############")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Salir ")
    print("###############")

    try:
        op = int(input("Seleccine una opción: "))

        if op < 1 or op > 4:
            print("Seleccione un numero del 1 al 4")

        if op == 4:
            exit()

        if op == 1:
            ej1.main()

        if op == 2:
            ej2.main()
        
        if op == 3:
            ej3.main()
    except ValueError:
        print("Deben ser numeros enteros")
