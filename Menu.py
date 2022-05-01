def MuestraMenu():
    op: int=0

    while op!=4:
        print("----------Eliga una opcion----------\n")
        print("1. Mostrar para cada variable el día y hora de menor y mayor valor.\n")
        print("2. Indicar la temperatura promedio mensual por cada hora.\n")
        print("3. Listar los valores de las tres variables para cada hora del día dado.\n")
        print("4.salir\n")
        op=int(input("Ingrese su opcion: "))

        return op
