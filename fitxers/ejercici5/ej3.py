def ej3(a,b):
    try:
        with open(f"taula-{a}.txt","r") as file:
            linea = file.readlines()
        print(linea[b-1])
    except FileNotFoundError:
        print("El fitxer no existeix")

if __name__=="ej3":
     print("Debes ejecutar el main para pasarle un numero")