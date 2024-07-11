#Ejercicio proveniente de la 3° Copa de Algoritmia de UADE de la cual participé en el año 2024
#Dicho ejercicio o desafio solicitaba realizar la simulacion de un partido de Hockey entre dos paises
#durante los juegos olimpicos de invierno, en lo cual tienen que figurar aproximadamente 50000 pases
# figurando si dicho pase fue o no exitoso, el minuto, y que jugadora lo realizó. 

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
cant_pases = 50000
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
#Inicio el bucle del partido (los 50000 pases)
while cant_pases > 0:
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
    cant_pases -= 1
#Consigo el directorio donde está guardado mi archivo Desafio1.py y lo guardo en la variable directorio
directorio = os.path.dirname(os.path.abspath(__file__))
#Junto la variable directorio con el nombre del archivo txt, en este caso Pases.txt
pasestxt = os.path.join(directorio, "Pases.txt")
#Compruebo si el archivo Pases.txt existe
if os.path.exists(pasestxt):
    #En caso de existir lo borro
    os.remove(pasestxt)
#Creo el archivo Pases.txt
archivo = open("Pases.txt", "x")
#paso por toda la lista de pases
for pase in lista_pases:
    #escribo el pase en una linea y bajo a otra linea
    archivo.write(f"{pase}\n")
#cierro el archivo
archivo.close()
#Ahora, en donde tenemos guardado nuestro archivo Desafio 1.py, debería existir
#un archivo txt con los resultados pedidos, y una extension de 50000 lineas



