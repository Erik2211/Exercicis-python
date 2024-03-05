def realizar(a):
    with open("llista.txt","r+") as file:
        linea = file.readlines()
        linea[a] = f"feta --> {linea[a]}  \n"
        file.seek(0)
        file.writelines(linea)
        
    print("Tasca realizada")
     