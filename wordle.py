#Wordle es un juego que consiste en la adivinanza de una palabra aleatoria y secreta, con 5 intentos
#para ello, donde iremos obteniendo pistas si las letras que componen dicha palabra son o no
#correctas, o si estan bien o mal posicionadas.
#Importo random para poder generar numeros aleatorios
import random
#Creo una lista con todas las palabras que pueden salir
palabras = ["arbol","avion","autos","palas","aleta","altar","arces","arpas","acilo","cabra","cajas","canas",
            "canto","carro","cejas","cenas","cepas","chile","china","cines","clara","clavo","costo",
            "crudo","curar","dados","dagas","datos","daños","dejar","denso","dotes","dunas","duros",
            "echar","hecho","elevo","enojo","error","estas","edito","fallo","falto","feria","fetos",
            "filas","finca","gafas","galas","gales","ganas","gases","ganar","giras","girar","gordo",
            "gorro","grave","grito","gasto","hacer","hasta","heces","hielo","ideas","india","islas",
            "jefas","jerga","julio","malos","marca","marco","menos","meter","moler","metro","morir",
            "monte","nacer","nadar","narro","naves","necio","niños","notas","nubes","obras","ocios",
            "ollas","ondas","onzas","opera","otros","ovulo","palas","pedir","pelea","pelos","peras",
            "perro","pesos","pilas","pinto","poder","quedo","quema","quito","reloj","rubio","rasco",
            "ratas","ratos","redes","remar","renos","renta","sabio","sacar","salir","selva","sanar",
            "sopas","secar","serio","sobar","sonar","subir","sucio","siete","tabla","tacos","tapas",
            "pazas","tener","tenis","terco","tipos","tiras","todas","todos","tomar","tonos","tonto",
            "toque","torpe","trote","vacas","vagos","valer","valor","veces","vedas","velas","vemos",
            "venas","venir","verde","viera","vigas","vinos","vivir","volar","votar","semen","tates",
            "yemas","yendo","yenes","yesca","yogur","zonas","zorro","zurdo","cosas","copas","papas",
            "algas","coral"]

#Hago que la palabra sea igual a una posicion aleatoria de la lista de palabras, dicha posicion se genera
#aleatoreamente usando la funcion random.randint, y elige un numero entre 0 y el largo de la lista, el cual
#saco usando la funcion len()
palabra = palabras[random.randint(0,len(palabras))]
intentos = 5
acierto = False
#inicio el while del juego, el cual va a seguir mientras tengas intentos y mientras no hayas acertado la palabra
while intentos != 0 and acierto != True:
    print(f"Intentos restantes: {intentos}")
    #creo respuesta y resultado, donde voy a almacenar temportalmente las letras correctas, incorrectas o mal
    #posicionadas (+:mal posicionada, -:incorrecta, *: correcta)
    respuesta = ''
    resultado= []
    intento = input("Ingrese una palabra de 5 letras: ")
    #corroboro que el largo de la palabra ingresada sea de 5, mediante la funcion len()
    while len(intento) != 5 or palabras.count(intento) == 0:
        print("Palabra ingresada no valida.")
        intento = input("Ingrese una palabra de 5 letras: ")
    #creo el for en el cual voy a revisar letra por letra    
    for i in range(0,5):
        #i es la posicion de la letra en la palabra, por ej, para "palas", la letra i = 3 es "l"
        #en este if confirmo si la letra i existe en la palabra
        if palabra.count(intento[i]) != 0:
            #si existe corroboro si está o no bien posicionada
            if palabra[i] == intento [i]:
                #si lo está, en la lista, ingreso en la posicion i un *
                resultado.insert(i,"*")
            else:
                #si no lo está, en la lista, ingreso en la posicion i un +
                resultado.insert(i,"+")
        else:
            #si no existe, en la posicion i, ingreso -
            resultado.insert(i,"-")
    #para cuando termine, voy a tener una lista con los resultados, por ej ["+", "-", "-", "+" , "*"]
    #ahora en este for, creo una palabra llamada respuesta, con los valores de la lista, por ej "+--+*"
    for l in resultado:
        respuesta += l
    #muestro en pantalla el intento que hice, y lo comparo con su resultado, por ej, si la palabra es "ceros"
    #y yo ingreso "clero" va a mostrar
    # clero
    # *-+++
    print(intento)
    print(respuesta)
    #compruebo si la palabra ingresada era la correcta
    if palabra == intento:
        acierto = True
    intentos -= 1
#muestro el resultado final, si acertaste o no
if acierto == True:
    print("Adivinaste la palabra!!")
else:
    print(f"La palabra era {palabra}")




