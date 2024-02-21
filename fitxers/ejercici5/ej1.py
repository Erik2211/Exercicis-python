def ej1(a):
    with open(f"taula-{a}.txt","w") as file:
        for i in range(1,11):
            res = a * i
            file.write(f"{a} * {i} = {res}\n")

if __name__=="__ej1__":
   print("Debes ejecutar el main para pasarle un numero")

    

        