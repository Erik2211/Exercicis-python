def mostrar_lista():
    try:
        with open(f"llista.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        print("El archivo llista.txt no existe")
