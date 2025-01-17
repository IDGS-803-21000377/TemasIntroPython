import os

def function1():
    os.system('cls')
    print("dame dos numeros:")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la suma es:", num1 + num2)
    input("presiona enter para volver al menu")

def function2():
    os.system('cls')
    print("dame dos numeros:")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la resta es:", num1 - num2)
    input("presiona enter para volver al menu")

def function3():
    os.system('cls')
    print("dame dos numeros:")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la multiplicacion es:", num1 * num2)
    input("presiona enter para volver al menu")

def function4():
    os.system('cls')
    print("dame dos numeros:")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la multiplicacion es:", num1 /num2)

    input("presiona enter para volver al menu")

def function5():
    os.system('cls')
    print("hasta luego")
    

def function6():
    print("opcion invalida, vuelve al menu")
    input("presiona enter para volver al menu")

def run():
    while True:
        os.system('cls')
        print("menu de opciones:")
        print("1- suma")
        print("2- resta")
        print("3- multiplicacion")
        print("4- division")
        print("5- salir")

        opcion = int(input("elige una opcion: "))

        if opcion == 1:
            function1()
        if opcion == 2:
            function2()
        if opcion == 3:
            function3()
        if opcion == 4:
            function4()
        if opcion >= 5:
            function5()
            break  
        else:
            function6()

if __name__ == "__main__":
    

    run()
