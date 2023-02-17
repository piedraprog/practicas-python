from os import system

salida = False 

while salida == False : 
    print('Bienvenido a la calculadora')
    print('para hacer las operaciones,\n selecciona un numero')
    print('para eso tienes que introducir un numero en consola y darle enter')
    print('-------------------------------------------------') 
    print('1.- Suma dos números') 
    print('2.- Resta dos números') 
    print('3.- Multiplica dos números') 
    print('4.- salir') 

    operacion = int(input('Elije la opcion: '))
    if operacion == 1 :
        system('cls') 
        n1 = int(input('ingrese el primer numero: '))
        n2 = int(input('ingrese el segundo numero: '))
        print("el resultado de la suma es: ",n1 + n2)

        
    if operacion == 2:
        system('cls') 
        n1 = int(input('ingrese el primer numero: '))
        n2 = int(input('ingrese el segundo numero: '))
        print("el resultado de la resta es:",n1 - n2)
    if operacion == 3:
        system('cls') 
        n1 = int(input('ingrese el primer numero: '))
        n2 = int(input('ingrese el segundo numero: '))
        print("el resultado de la multiplicación es: ",n1 * n2)

    if operacion == 4:
        system('cls') 
        salida = True
    
    