abecedario = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

numero = int(input("Ingresá el número de patente que querés: "))

contador = 0

for l1 in abecedario:
    for l2 in abecedario:
        for l3 in abecedario:
            for n1 in range(10):
                for n2 in range(10):
                    for n3 in range(10):
                        if contador == numero:
                            patente = f"{l1}{l2}{l3} {n1}{n2}{n3}"
                            print("Patente generada:", patente)
                            quit()
                        contador = contador + 1