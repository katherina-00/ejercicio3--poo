from tkinter.messagebox import RETRY

class Registro:
    __temperatura: 0
    __humedad: 0
    __presionAtmosferica: 0

    def __init__(self, temperatura,humedad,presionAtmosferica):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presionAtmosferica=presionAtmosferica
    
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad

    def getPresionAtmosferica(self):
        return self.__presionAtmosferica

    def muestraMayor(self,lista,dia,horas):
        maximoT=int(0)
        maximoH=int(0)
        maximoP=int(0)
        for dia in range (len(lista)):
                for horas in range (len(lista[dia])):
                    if lista[dia][horas].getTemperatura()>maximoT:
                        maximoT=lista[dia][horas].getTemperatura()
                        auxDia=dia
                        auxHora=horas

                    if lista[dia][horas].getHumedad()>maximoH:
                        maximoH=lista[dia][horas].getHumedad()
                        auxDia1=dia
                        auxHora1=horas
                    
                    if lista[dia][horas].getPresionAtmosferica()>maximoP:
                        maximoP=lista[dia][horas].getPresionAtmosferica()
                        auxDia2=dia
                        auxHora2=horas
        print('-' * 60)
        print("Temperatura Maxima: {} Dia: {} Hora: {}".format(maximoT,auxDia+1,auxHora+1))
        print("Humedad Maxima: {} Dia: {} Hora: {}".format(maximoH,auxDia1+1,auxHora1+1))
        print("Presion Atmosferica Maxima: {} Dia: {} Hora: {}".format(maximoP,auxDia2+1,auxHora2+1))
        print('-' * 60)
    
    def muestraMenor(self,lista,dia,horas):
        minimoT=int(9999)
        minimoH=int(9999)
        minimoP=int(9999)
        for dia in range (len(lista)):
                for horas in range (len(lista[dia])):
                    if lista[dia][horas].getTemperatura()<minimoT:
                        minimoT=lista[dia][horas].getTemperatura()
                        auxDia=dia
                        auxHora=horas

                    if lista[dia][horas].getHumedad()<minimoH:
                        minimoH=lista[dia][horas].getHumedad()
                        auxDia1=dia
                        auxHora1=horas
                    
                    if lista[dia][horas].getPresionAtmosferica()<minimoP:
                        minimoP=lista[dia][horas].getPresionAtmosferica()
                        auxDia2=dia
                        auxHora2=horas

        print("Temperatura Minima: {} Dia: {} Hora: {}".format(minimoT,auxDia+1,auxHora+1))
        print("Humedad Minima: {} Dia: {} Hora: {}".format(minimoH,auxDia1+1,auxHora1+1))
        print("Presion Atmosferica Mininima: {} Dia: {} Hora: {}".format(minimoP,auxDia2+1,auxHora2+1))
        print('-' * 60)

    def TempPromedio(self,lista,dia,horas):

        acumLista = [0.0]*horas
        acum: float=0.0
        for dia in range(len(lista)):
            for horas in range(len(lista[dia])):
                acum+=lista[dia][horas].getTemperatura()
                acumLista[horas]=acum

        for i in range(len(acumLista)):
            print("Hora: {} Temp promedio: {:.2f} ".format(i+1,(acumLista[i]/dia)/horas))

    def listaConFormato(self,lista,diaBuscado):

        for dia in range(len(lista)):
            if dia==diaBuscado:
                print ("{:<10} {:<10} {:<10} {:<12}".format('Hora','Temperatura','Humedad','Presion'))
                for horas in range(len(lista[dia])):
                    print("{:<10} {:<10} {:<10} {:<10}".format(
                    horas,lista[dia][horas].getTemperatura(),lista[dia][horas].getHumedad(),
                    lista[dia][horas].getPresionAtmosferica()))
