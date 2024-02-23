import operaciones as oper

print("Benvingut a la Calculadora d'Operacions Bàsiques!")

print("1. Suma")
print("2. Resta")
print("3. Multiplicació")
print("4. Divisió")

op=int(input("eleccione una operació (1/2/3/4): "))

if op < 1 or op > 4:
    print("Debes seleccionar un numero del 1 al 4")
    exit()
    

num1=int(input("Ingresse el primer número: "))
num2=int(input("Ingresse el segon número: "))
print()

if op == 1:
    print("Resultat de la suma: ",oper.suma(num1,num2) )

if op == 2:
    print("Resultat de la resta: ",oper.resta(num1,num2))

if op == 3:
    print("Resultat de la multiplicacio: ",oper.multiplicacio(num1,num2))

if op == 4:
    print("Resultat de la divisio: ",oper.divisio(num1,num2))


