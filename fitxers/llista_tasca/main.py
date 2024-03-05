import menu
import mostrar_lista
import afegir_tasca
import realitzar_tasca

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
        mostrar_lista.mostrar_lista()

    if opc == 2:
        linea = input("Añade la tasca: ")
        afegir_tasca.add_task(linea)
    
    if opc == 3:
        with open("llista.txt","r") as file:
            x = 0    
            for i in file.readlines():
                print(f"{x}- {i}")
                x = x + 1
        feta = int(input("Seleccione la tasca realizada: "))
        realitzar_tasca.realizar(feta)
        
            