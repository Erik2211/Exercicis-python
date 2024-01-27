## Ejercici 1: Calculadora d’Operacions Bàsiques 

Crea un programa en Python que conste de dos arxius: calculadora.py i operaciones.py.  

- operaciones.py  
  
Definix un mòdul anomenat operacions que continga funcions per a realitzar les següents operacions:  

 -Suma - Resta - Multiplicació - Divisió  

Cada funció ha d’acceptar dos paràmetres i retornar el resultat de l’operació corresponent.  

- calculadora.py  

En l’arxiu principal, calculadora.py, importa el mòdul operacions.  

Crea un menú simple que permeta a l’usuari seleccionar una operació (suma, resta, multiplicació,
divisió) i ingressar dos números per a realitzar l’operació triada.  

Utilitza les funcions del mòdul operacions per a realitzar l’operació seleccionada i imprimeix el resul-
tat.  

Exemple d’Execució:

```
Benvingut a la Calculadora d'Operacions Bàsiques!

 1. Suma
 2. Resta
 3. Multiplicació
 4. Divisió
 eleccione una operació (1/2/3/4): 1
 Ingresse el primer número: 5
 Ingresse el segon número: 3

 Resultat de la suma: 8
```
## Ejercici 2:Gestor de Tasques 

Crea un programa en Python que implemente un gestor simple de tasques. Dividix la teua solució en dos arxius: tareas.py i gestor_tareas.py.  

- tareas.py
- Definix un mòdul anomenat tasques que continga funcions per a realitzar les següents operacions:
- Agregar una tasca
- Marcar una tasca com completada
- Mostrar totes les tasques (pendents i completades)

Cada tasca ha de tindre un identificador únic, una descripció i un estat que indique si està completada
o no.  

- gestor_tareas.py
  
En l’arxiu principal, gestor_tareas.py, importa el mòdul tasques.  

Crea un menú que permeta a l’usuari realitzar les següents accions:

- Agregar una nova tasca
- Marcar una tasca com completada
- Mostrar totes les tasques

Exemple d’Execució:

```
Benvingut al Gestor de Tasques!

 1. Agregar nova tasca
 2. Marcar tasca com completada
 3. Mostrar totes les tasques
 4. Eixir

 Seleccione una opció (1/2/3/4): 1
 Ingresse la descripció de la nova tasca: Fer la compra

 Tasca agregada amb éxit!

 Agregar nova tasca
 2. Marcar tasca com completada
 3. Mostrar totes les tasques
 4. Eixir

 Seleccione una opció (1/2/3/4): 3
 Llista de tasques:

 - [ ] ID: 1 - Fer la compra

 1. Agregar nova tasca
 2. Marcar tasca com completada
 3. Mostrar totes les tasques
 4. Eixir

 Seleccione una opció (1/2/3/4): 2
 Ingresse l'ID de la tasca que desitja marcar com completada: 1

 Tasca marcada com completada amb éxit!

 1. Agregar nova tasca
 2. Marcar tasca com completada
 3. Mostrar totes les tasques
 4. Eixir

 Seleccione una opció (1/2/3/4): 3
 Llista de tasques:

 - [x] ID: 1 - Fer la compra (Completada)

 1. Agregar nova tasca
 2. Marcar tasca com completada
 3. Mostrar totes les tasques
 4. Eixir

 Seleccione una opció (1/2/3/4): 4
 Fins ara!
```

