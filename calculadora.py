
def suma(a , b):
    return a + b

def resta(a , b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a , b):
    return a / b

def calculadora():
    while True:
        print("¿que operacion desea realizar?")
        print("1- suma")
        print("2- resta")
        print("3- multiplicacion")
        print("4- division")
        print("5- salir")
        
        opcion = input("elige una opcion: ")
        if opcion == "5":
            print("¡Hasta pronto!")
            break
            
        
        num1 = int(input("INTRODUCE EL PRIMER NUMERO: "))
        num2 = int(input("INTRODUCE EL SEGUNDO NUMERO: "))
                
                
        if opcion == "1":
            print(f"El resultado de la suma es: {suma(num1 , num2)}")
        
        elif opcion == "2":
            print(f"El resultado de la resta es: {resta(num1 , num2)}")
        
        elif opcion == "3":
            print(f"El resultado de la multiplicacion es: {multiplicacion(num1 , num2)}")
        
        elif opcion == "4":
            print(f"El resultado de la division es: {division(num1 , num2)}")
        
        else:
            print("Esa opcion no es valida, vuelve a intentar")    

print("-----------------------------")        
calculadora()