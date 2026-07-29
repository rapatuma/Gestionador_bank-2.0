import time

dicc  = {

    "8298355868": " Cristina Gabriela Mejia Morillo",
    "8495225868": " jose Gabriel ortega mejia",
    "8495995868": " Josefani Gabriela Ortega Mejia",
    "8494575868": "Jose Ortega Corniel"
}



historial = []


cuenta_tercero = 123456
cuenta_personal = 123
balance_personal = 10000
primer_pin = 1234

name = input("ingrese su nombre: ")

while name == "":
    print("Debe ingresar su nombre para continuar")
    name = input("ingrese su nombre: ")

log_in = int(input("ingrese su pin: "))
time.sleep(2)
print("verificando su pin...")
time.sleep(2)
while log_in != primer_pin:
   print("El pin es incorrecto.") 
   log_in = int(input("ingrese su pin: "))
   time.sleep(2)
   print("verificando su pin...")
   time.sleep(2)

log_in_cuenta = int(input("ingrese su numero de cuenta: "))
time.sleep(2)
print("verificando su cuenta...")
time.sleep(2)
while log_in_cuenta != cuenta_personal:
   print("El numero de cuenta es incorrecto.")
   log_in_cuenta = int(input("ingrese su numero de cuenta: "))
   time.sleep(2)
   print("verificando su cuenta...")
   time.sleep(2)


print(f"Bienvenido Sr {name} a su cuenta")


while True:
    print("""
    Bienvendo a este gestionador de cajero automatico....

     
    1.- Revisar balance
    2.- transferencia
    3.- Cambiar PIN
    4.- Retirar dinero
    5.- Depositar dinero 
    6.- Historial 
    7.- Poner recargas
    8- Salir del programa

""")
    
    opcion = input(f"seleccione el numero de la opcion que desea realizar SR {name}: ")


    match opcion:
        case "1":
         print("procesando", end="", flush=True)
         for _ in range(5):
            time.sleep(1)
            print(".", end="", flush=True)
         print(f" |su balance actual es: {balance_personal:.2f}| ")
         historial.append(f"Usted reviso su balance y es de: |{balance_personal:.2f}|")
        
        case "2":
           print("Procesando", end="", flush=True)
           for _ in range(5):
             time.sleep(1.3)
             print(".", end="", flush=True)
           cuenta1 = int(input("| Introduzca la cuenta de la persona a la que le desea transferir: "))
           if cuenta1 == cuenta_tercero:
               print("Exelente, ya usted puede transferir")
               time.sleep(2)
               deposito = int(input("Introzduzcala cantidad de dinero que desea transferir:"))
               print("Procesando", end="", flush=True)
               for _ in range(5):
                time.sleep(1.2)
                print(".", end="", flush=True)
               if deposito > balance_personal:
                    print("no puede transferir esa cantidad de dinero, su balence es insuficiente")
               else:
                    balance_personal -= deposito
                    print(f"transferencia hecha correctamente,  |este es su balence actual: {balance_personal}|")  
                    historial.append(f"Usted transfirio {deposito} a la cuenta {cuenta1} y su balence actual es: |{balance_personal}|")

           else:
               print("Cuenta no encontrada.....")
    
        
        case "3":
            print("Para cambiar el pin, usted debe ingreser su pin actual")
            pin = int(input("ingrese su pin actual:"))
            print("Verificando pin", end="", flush=True)
            for _ in range(5):
                time.sleep(1.2)
                print(".", end="", flush=True)
            if  pin == primer_pin:
                print("Exelente, ahora ya usted puede cambiar su Pin") 
                nuevo_pin = int(input("ingrese su nuevo pin: "))
                print("Actualizando pin ", end="", flush=True)
                for _ in range(5):
                    time.sleep(2)
                    print(".", end="", flush=True)
                primer_pin = nuevo_pin
                print("su pin ha sido cambiado correctamente")
                historial.append(f"Se ha realizado un cambio de pin. El nuevo pin es: {nuevo_pin}")
            else:
                print("Debe ingrese su contraseña correctamente")
                

        case "4":
            retiro = float(input("cual es la cantidad que usted desea retirar: "))
            print("Procesando retiro", end="", flush=True)
            for _ in range(5):
             time.sleep(2)
             print(".", end="", flush=True)
            if retiro > balance_personal:
                print("solo puedes retirar de acorde al balence de tu cuenta.")

            else:
                balance_personal -= retiro
                print("|Bien, Retirando dinero correctamente....|")
                historial.append(f"Usted retiró |{retiro} |")

        case "5":
            cuenta = int(input("Ingrese el numero de cuenta: "))
            print("Validando", end="", flush=True)
            for _ in range(5):
                time.sleep(1.2)
                print(".", end="", flush=True)
            if cuenta == cuenta_personal:
                print("Cuenta correcta, ahora puede depositar dinero")
                depositar = int(input("Ingrese el deposito: "))
                print("Procesando", end="", flush=True)
                for _ in range(5):
                    time.sleep(1.1)
                    print(".", end="", flush=True)
                balance_personal += depositar
                print(f"|Su balence actual es de:  {balance_personal}|")
                historial.append(f"Usted ha recibido un deposito de {depositar}")
            else:
                print("Cuenta incorrecta.")


        case "6":
            print(f" Historial de movimientos:| {historial}|")


        case "7":
            recarga = input("Digite su numero de de telefono: ")
            if recarga in dicc:
                print(f"bien, su numero ha sido encontrado: numero de  |{dicc[recarga]}|")
                montoRecarga = int(input("Digite el monto de la recarga: ")) 
                print("Procesando recarga", end="", flush=True)
                for _ in range(5):
                    time.sleep(1.2)
                    print(".", end="", flush=True)
                if montoRecarga > balance_personal or montoRecarga < 50:
                    print("No puede realizar la recarga, su balence es insuficiente o el monto es menor a 50 pesos")
                else:

                    time.sleep(2)
                    balance_personal -= montoRecarga
                    print("Recarga realizada correctamente.")
                    historial.append(f"Usted ha realizado una recarga al numero {recarga} de {montoRecarga}")
        
            else:
                print("Numero no encontrado..")


        case "8":
         print("Gracias por utilizar nuestros servicios... ")
         break


        case _:
            print("Opcion no valida, por favor seleccione una opcion valida")
        
