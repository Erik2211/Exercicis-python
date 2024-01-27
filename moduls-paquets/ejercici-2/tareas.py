import time
tasques=[]
ids = [] 
tasca_completada = []

tasca="- []"
tasca_c="- [X]"

cont = 1
def agregar_tasca():
    global cont
    tasca=input("Ingresse la descripció de la nova tasca: ")
    tasques.append(tasca)
    ids.append(cont)
    cont = cont + 1 




def marcar_tasca() :
    id = input("Ingrese el ID de la tasca que desitja marcar com completada: ")
    tasca_completada.append(int(id))
    

def mostrar_tasques():
    for a,b in zip(ids,tasques):
        if a in tasca_completada:
            print(tasca_c,a,b)
        else:
            print(tasca,a,b)
    time.sleep(3)




