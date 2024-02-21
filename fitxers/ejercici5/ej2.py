def ej2(a):
    try:
        f = open(f"taula-{a}.txt","r")
    except FileNotFoundError:
        print("El fitxer no existeix")
    else:
        print(f.read())
        f.close()

if __name__=="__ej2__":
     print("Debes ejecutar el main para pasarle un numero")