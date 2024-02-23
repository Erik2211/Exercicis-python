def add_task(a):
    try:
        with open(f"llista.txt","a") as file:
            file.write(a + "\n")
    except FileNotFoundError:
        print("El archivo llista.txt no exise. Crea ese fichero")
    print("Tarea añadida")
