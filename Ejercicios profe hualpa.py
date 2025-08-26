print("---Ejercicios Profe Hualpa---")

#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
print("--Ejercicio 6--")
print("Ingresá tus 3 notas de los parciales")
nota1 = int(input("Parcial 1:"))
nota2 = int(input("Parcial 2:"))
nota3 = int(input("Parcial 3:"))
promedio_parcial = (nota1 + nota2 + nota3) / 3
print("")

print("Ingresá tu calificación en el examen final")
nota_examen = int(input(""))
print("")

print("Ingresá tu calificación en el trabajo final")
nota_trabajo = int(input(""))
print("")

calificacion_final = (promedio_parcial * 0.55) + (nota_examen * 0.30) + (nota_trabajo * 0.15)
calificacion_final = round(calificacion_final)
print(f"Tu calificación final es:{calificacion_final}")
print("")

#Ejercicio 7: Conversión de divisas
print("--Ejercicio 7--")
dolar_pesoColombiano = 4023.40
dolar_pesoArgentino = 1357.54
dolar_euro = 0.86

dolar = int(input("Ingresá una cantidad de dólares:"))

dolar_pesoColombiano = dolar * dolar_pesoColombiano
dolar_pesoArgentino = dolar * dolar_pesoArgentino
dolar_euro = dolar * dolar_euro
print(f"${dolar} dólar/dólares a peso colombiano ={dolar_pesoColombiano}")
    
print(f" ${dolar} dólar/dólares a peso argentino = {dolar_pesoArgentino}")
    
print(f" ${dolar} dólar/dólares a peso argentino = {dolar_euro}")
print("")

#Ejercicio 8: Viaje en auto
print("--Ejercicio 8--")

distancia = int(input("Ingrese la distancia a recorrer: "))
precio_litro = int(input("Ingrese el precio de la gasolina por litro: "))

litros_necesarios = (distancia / 100) * 8
costo_gasolina = litros_necesarios * precio_litro
tiempo_viaje = distancia / 90
tiempo_viaje = round(tiempo_viaje,1)

print(f"La cantidad de litros necesarios para poder viajar es de: {litros_necesarios}")
print(f"El costo de la gasolina es de: {costo_gasolina}")
print(f"El tiempo promedio en horas si la velocidad es de 90km/h: {tiempo_viaje}")
print("")

#Ejercicio 9: Préstamo bancario
print("--Ejercicio 9--")

prestamo = int(input("Ingresá el monto del préstamo"))
interes = 0.02
monto_devolver = monto * ((1 + interes)**12)
valor_cuota = monto_devolver / 12
print(f"La cantidad total a devolver del préstamo con un 2% de interés es de: {monto_devolver}")
print(f"El valor de cada cuota es de: {valor_cuota}")