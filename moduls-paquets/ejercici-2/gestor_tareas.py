import time
import tareas 

def menu():
    print("1. Agregar nova tasca")
    print("2. Marcar tasca com completada") 
    print("3. Mostrar totes les tasques") 
    print("4. Eixir")

while True:
    menu()
    
    op=int(input("Seleccione una opció (1/2/3/4): "))
    if op < 1 or op > 4:
        print("Debes seleccionar solo numeros del 1 al 4")
        time.sleep(2)
    # Comprobamos qual es la opcion para llamar a la funcion
    if op == 4: 
        exit()
    if op == 1:
        tareas.agregar_tasca()    
        print("Tasca agregada amb éxit")
        time.sleep(1)

    if op == 2:
        tareas.marcar_tasca()

    if op == 3: 
        tareas.mostrar_tasques() 
        