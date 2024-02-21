# Escriure un programa que demane dos números n i m entre 1 i 10, llija el fitxer taula-n.txt amb la
# taula de multiplicar d’eixe número, i mostre per pantalla la línia m del fitxer. 
# Si el fitxer no existix ha de mostrar un missatge per pantalla informant d’això.


def main():
    n = int(input("Diges un numero entre el 1 i el 10: "))   
    m = int(input("Diges un numero entre el 1 i el 10: "))

    try:
        with open(f"taula-{n}.txt","r") as file:
            linea = file.readlines()
        print(linea[m-1])      
    except FileNotFoundError:
            print("El fitxer no existeix")

if __name__=="__main__":
     main()