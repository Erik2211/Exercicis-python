
# Escriure un progama que demane un nombre enter entre 1 i 10 i guarde en un fitxer amb el nom
# taula-n.txt la taula de multiplicar d’eixe número, on n és el número introduït.



num = int(input("Diges un numero entre el 1 i el 10: "))
with open(f"taula-{num}.txt","w") as file:
    for i in range(1,11):
        res = num * i
        file.write(f"{num} * {i} = {res}\n")
with open(f"taula-{num}.txt","r") as file:
    print(file.read())    