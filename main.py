import csv
from ClaseRegistro import Registro
import Menu
if __name__=="__main__":

    dias=30
    horas=24
    lista= [[0 for i in range(horas)] for j in range (dias)]

    with open("mes1.csv","r") as file:
        reader=csv.reader(file,delimiter=",")
        for fila in reader:
            dia=int(fila[0])
            hora=int(fila[1])
            temp=float(fila[2])
            hume=int(fila[3])
            pres=int(fila[4])
            lista[dia-1][hora-1]=Registro(temp,hume,pres)

    op=Menu.MuestraMenu()
    while op!=4:
        if op==1:
            lista[dia-1][horas-1].muestraMayor(lista,dia,horas)
            lista[dia-1][horas-1].muestraMenor(lista,dia,horas)
        elif op==2:
            lista[dia-1][horas-1].TempPromedio(lista,dia,horas)
        elif op==3:
            dia=int(input("Ingrese dia a consultar: "))
            lista[dia-1][horas-1].listaConFormato(lista,dia-1)

        op=Menu.MuestraMenu()
