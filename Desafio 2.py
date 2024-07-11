#Ejercicio proveniente de la 3° Copa de Algoritmia de UADE de la cual participé en el año 2024
#Este ejercicio es una ampliacion del Desafio 1, en el cual habia que agregar la creación de un archivo
#que muestre el rendimiento individual de cada jugadora en el partido usando como datos los generados
# y guardados en Pases.txt. 

#En este ejercicio y dado a los ejemplos mostrados y una busqueda en internet,
#vimos que los partidos de hockey suelen durar 2 tiempos de 35m, más 15 extra,
#más penales, por ende, nosotros asumimos un partido de 90m desglosado en 
#dos tiempos de 90m
#importo las librerias random, para generar numeros aleatorios, y os para obtener un directorio
import random
import os
#Creo la lista de jugadores de Argentina
argentina = [["Juliana Gimenez", 15],
             ["Romina Hernandez", 4],
             ["Camila Velasquez", 23],
             ["Sofia Martinez", 10],
             ["Estefania Yucra", 11],
             ["Fernanda Trimarco", 28],
             ["Laura Alvarez", 29],
             ["Felicia Dangara", 22],
             ["Beatriz Nuñez", 9]]
#Creo la lista de jugadores de Australia
australia = [["Hannah Maier", 10],
             ["Leonie Wieser", 11],
             ["Amelie Wimmer", 12],
             ["Anna Pichler", 13],
             ["Flora Wimmer", 14],
             ["Eva Bauer", 15],
             ["Emma Huber", 16],
             ["Sophie Wolf", 17],
             ["Rosalie Binder", 18]] 
#declaro variables
lista_pases=[]

#Creo una funcion para registrar los pases realizados
def pase_realizado(pais, equipo):
    #guardo en jugador, una lista de la lista de jugadores, ya sea argentina o australia
    jugador = equipo[random.randrange(0,9)]
    #Genero si el pase fue o no concretado (1 concretado, 0 no concretado)
    concretado = random.randrange(0,2)
    #guardo en que minuto se hizo el pase, desde el minuto 0 hasta el 90
    tiempo = random.randrange(0,91)
    #devuelvo un string con todos los datos ordenados
    return(f"{pais} ; {jugador[1]} ; {jugador[0]} ; {concretado} ; {tiempo}")
#creo la funcion solicitada en el desafio 2
def contar_pases_y_efectividad():
    #Creo una lista lineas, donde guardo las lineas del txt creado anteriormente, lo separo según fines de linea y cierro el archivo
    archivo = open(pasestxt,"r")
    lineas = archivo.read().split("\n")
    archivo.close
    #borro la ultima linea del archivo dado a que es un string vacio
    del lineas[len(lineas)-1]
    datos = []
    #reviso la lista generada y transformo los string en  listas separado por " ; "
    for linea in lineas:
        datos.append(linea.split(sep = " ; "))
    #Ordeno datos por nombres de jugadores y por paises
    datos = sorted(datos, key=lambda x: x[2])
    datos = sorted(datos, key=lambda x: x[0])
    datos.append(["final", 0, "final",0,0]) #Marco el final de la lista para así, en el if, no pierdo los resultados de la ultima jugadora
    armado = {"Argentina": [], "Australia": []}
    #declaro las variables iniciales que voy a usar para crear el resultado final de armado
    pase_bien = 0
    pase_mal = 0
    p = datos[0][0] #pais
    num = datos[0][1] #numero
    n = datos[0][2] #nombre
    #hago un for para pasar de datos en datos
    for dato in datos:
        #si el nombre del jugador es igual al nombre guardado anteriormente, anoto si el pase que dio fue bueno o malo, sumandolo
        if dato[2] == n:
            if int(dato[3]) == 1:
                pase_bien += 1
            else:
                pase_mal +=1
        #En caso de que cambie de jugador, es decir, que se cambie el nombre, realizo un append a armado formando los datos pedidos
        else:
            armado[str(p)].append({"numero": num,"nombre": n,"cantidad pases": (pase_bien+pase_mal),"pases bien":pase_bien,"pase mal":pase_mal,"porcentaje": ((pase_bien * 100)/(pase_bien+pase_mal))})
            #Reinicio las variables de seguimiento y corroboro un pase para no perder ese paso
            p = dato[0] #pais
            num = dato[1] #numero
            n = dato[2] #nombre
            pase_bien = 0
            pase_mal = 0
            if int(dato[3]) == 1:
                pase_bien += 1
            else:
                pase_mal += 1
    #Ordeno la lista según los porcentajes y tambien redondeo los porcentajes a dos digitos despues de la coma
    for pais, jugadores in armado.items():
        for jugador in jugadores:
            jugador['porcentaje'] = round(jugador['porcentaje'], 2)
        armado[pais] = sorted(jugadores, key=lambda x: x['porcentaje'], reverse=True)
    return armado
#Inicio el bucle del partido (los 50000 pases)
for pases in range(0,50000):
    #Genero que equipo hizo el pase (0 Argentina, 1 Australia)
    equipo = int(random.randrange(0,2))
    if equipo == 0:
        #Guardo en la lista lista_pases el return de pase_realizado() ingresandole que argentina realizó el pase
        #y la lista de jugadoras argentinas
        lista_pases.append(pase_realizado("Argentina", argentina))
    else:
        #Guardo en la lista lista_pases el return de pase_realizado() ingresandole que australia realizó el pase
        #y la lista de jugadoras argentinas
        lista_pases.append(pase_realizado("Australia", australia))

#Consigo el directorio donde está guardado mi archivo Desafio1.py y lo guardo en la variable directorio
directorio = os.path.dirname(os.path.abspath(__file__))
#Junto la variable directorio con el nombre del archivo txt, en este caso Pases.txt
pasestxt = os.path.join(directorio, "Pases.txt")
#Creo el archivo Pases.txt
archivo = open(pasestxt, "w")
#paso por toda la lista de pases
for pase in lista_pases:
    #escribo el pase en una linea y bajo a otra linea
    archivo.write(f"{pase}\n")
#cierro el archivo
archivo.close()

print(contar_pases_y_efectividad())

#Ahora, en donde tenemos guardado nuestro archivo Desafio 1.py, debería existir
#un archivo txt con los resultados pedidos, y una extension de 50000 lineas



