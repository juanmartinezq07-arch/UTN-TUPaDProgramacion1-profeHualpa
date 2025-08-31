#Ejercicio 1 — Clasificación de impuestos

nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese su ingreso anual: "))
print("")
if ingresos < 500000 :
    print("No paga impuestos")
    impuestos = "Ninguno"
elif ingresos >= 500000 and ingresos < 2000000 :
    impuestos = ingresos * 0.15
elif ingresos >= 2000000 and ingresos < 5000000 :
    impuestos = ingresos * 0.20
elif ingresos >= 5000000 :
    impuestos = ingresos * 0.35

print(f"Nombre completo: {nombre}\nEdad: {edad}\nIngresos anuales: {ingresos}\nImpuesto a pagar: {impuestos}")
print("")

#Ejercicio 2 — Sistema de calificaciones con promoción
from colorama import init, Fore, Style
nombre = str(input("Ingrese su nombre: "))
legajo = int(input("Ingrese su legajo: "))
nota1 = int(input("Ingrese sus 3 notas (entre 0 y 10)\nNota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0:
    print("Nota/s Incorrecta/s")
else:
    promedio = (nota1 + nota2 + nota3) / 3
    if nota1 < 4 or nota2 < 4 or nota3 < 4:
        estado = str("Desaprobado Directo")
    elif promedio < 6 :
        estado = str("Desaprobado")
    elif promedio == 6 or promedio == 7 :
        estado = str("Aprobado con final")
    elif promedio >= 8 :
        estado = str("Promocionado")
    print("Nombre: " + Fore.BLUE + nombre)
    print(Fore.WHITE + "Legajo: " + Fore.CYAN + str(legajo))
    if estado == "Desaprobado Directo" :
        print(Fore.WHITE + "Estado académico: "+ Fore.RED + estado )
    elif estado == "Desaprobado":
        print(Fore.WHITE + "Estado académico: " + Fore.RED + estado)
    elif estado == "Aprobado con final" :
        print(Fore.WHITE + "Estado académico: " + Fore.YELLOW + estado)
    elif estado == "Promocionado" :
        print(Fore.WHITE + "Estado académico: " + Fore.GREEN + estado)

print("")

#Ejercicio 3 — Simulador de cajero automático

print("----Simulador de cajero automático----")
nombre_usuario = str(input(Fore.WHITE + "Ingrese su nombre de usuario: "))
if nombre_usuario.lower() == "cancelar":
    print("Operación cancelada por el usuario.")
else:
    pin = input("Cree un PIN: ")
    saldo_inicial = 25000

    pin_valido = False
    validar_pin = input("Ingrese su PIN para poder operar: ")
    if validar_pin.lower() == "cancelar":
        print("Operación cancelada por el usuario.")
    elif validar_pin == pin:
        pin_valido = True
        print("PIN correcto. Puede continuar operando.")
    elif validar_pin != pin:
            print("PIN INCORRECTO. Intente nuevamente:")
            validar_pin = input("")
            if validar_pin.lower() == "cancelar":
                print("Operación cancelada por el usuario.")
            elif validar_pin == pin:
                pin_valido = True
            elif validar_pin != pin:
                print("PIN INCORRECTO. Intente nuevamente:")
                validar_pin = input("")
                if validar_pin.lower() == "cancelar":
                    print("Operación cancelada por el usuario.")
                elif validar_pin == pin:
                    pin_valido = True
                else:
                    print("Máximo intento alcanzado.")

    if pin_valido:
        monto_retiro = input("Ingrese el monto a retirar (tiene que ser múltiplo de 1000): ")
        if monto_retiro.lower() == "cancelar":
            print("Operación cancelada por el usuario.")
        else:
            monto_retiro = int(monto_retiro)
            if monto_retiro > saldo_inicial:
                print("Monto de retiro mayor al saldo")
            elif monto_retiro % 1000 != 0:
                print("El monto debe ser múltiplo de 1000")
            elif monto_retiro > 20000:
                comision = monto_retiro * 0.02
                total = monto_retiro + comision
                if saldo_inicial - total < 0:
                    print("Saldo no suficiente cobrando extra de comisión")
                else:
                    saldo_inicial -= total
                    print(f"Retiro exitoso. Se cobró una comisión de ${comision:.2f}. Saldo restante: ${saldo_inicial:.2f}")
            else:
                saldo_inicial -= monto_retiro
                print(f"Retiro exitoso. Saldo restante: ${saldo_inicial:.2f}")