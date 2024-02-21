# Escriure un programa que demane un nombre enter entre 1 i 10, llija el fitxer taula-n.txt amb la
# taula de multiplicar d’eixe número, done n és el número introduït, i la mostre per pantalla. Si el fitxer
# no existix ha de mostrar un missatge per pantalla informant d’això.

def main():
    num = int(input("Diges un numero entre el 1 i el 10: "))   
    try:
        f = open(f"taula-{num}.txt","r")   
    except FileNotFoundError:
        print("El fitxer no existeix")
    else:
        print(f.read())
        f.close()

if __name__=="__main__":
    main()
