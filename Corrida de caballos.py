import random
import time
import os


def mostrar_tablero(tablero):
    for fila in tablero:
        for columna in fila:
            print(columna,end="")
        print()
def actualizar_tablero(tablero,caballo1,caballo2,caballo3,caballo4,caballo5):
    #caballo1
    mov = random.randint(1,3)
    tablero[1][caballo1] = " "
    caballo1 += mov
    tablero[1][caballo1] = "*"
    #caballo2
    mov = random.randint(1,3)
    tablero[2][caballo2] = " "
    caballo2 += mov
    tablero[2][caballo2] = "*"
    #caballo3
    mov = random.randint(1,3)
    tablero[3][caballo3] = " "
    caballo3 += mov
    tablero[3][caballo3] = "*"
    #caballo4
    mov = random.randint(1,3)
    tablero[4][caballo4] = " "
    caballo4 += mov
    tablero[4][caballo4] = "*"
    #caballo5
    mov = random.randint(1,3)
    tablero[5][caballo5] = " "
    caballo5 += mov
    tablero[5][caballo5] = "*"
    mostrar_tablero(tablero)
    return(caballo1,caballo2,caballo3,caballo4,caballo5,tablero)
def juego(billetera):
    tablero = [
        [" ","╔","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","╗"],
        ["1","║","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
        ["2","║","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
        ["3","║","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
        ["4","║","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
        ["5","║","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
        [" ","╚","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","╝"]
    ]
    caballo1 = 2
    caballo2 = 2
    caballo3 = 2
    caballo4 = 2
    caballo5 = 2
    victoria = 60
    game = True

    micaballo = int(input("A cual caballo desea apostar? (1-5): "))
    while micaballo < 1 or micaballo > 5:
        micaballo = int(input("Caballo invalido, ingrese de nuevo (1-5): "))
    apuesta = int(input("Cuanto desea apostar?: "))
    while apuesta > billetera or apuesta < 1:
        apuesta = int(input("Monto ingresado invalido, ingrese nuevo monto: "))
    billetera -= apuesta
    os.system("cls")
    while game == True:
        caballo1,caballo2,caballo3,caballo4,caballo5,tablero = actualizar_tablero(tablero,caballo1,caballo2,caballo3,caballo4,caballo5)
        time.sleep(0.5)
        os.system("cls")
        if caballo1 >= victoria or caballo2 >= victoria or caballo3 >= victoria or caballo4 >= victoria or caballo5 >= victoria:
            game = False
    if caballo1 >=  victoria:
        print("El ganador es el caballo Numero 1!!!")
        ganador = 1
    elif caballo2 >=  victoria:
        print("El ganador es el caballo Numero 2!!!")
        ganador = 2
    elif caballo3 >=  victoria:
        print("El ganador es el caballo Numero 3!!!")
        ganador = 3
    elif caballo4 >=  victoria:
        print("El ganador es el caballo Numero 4!!!")
        ganador = 4
    elif caballo5 >=  victoria:
        print("El ganador es el caballo Numero 5!!!")
        ganador = 5
    if ganador == micaballo:
        billetera = billetera + (apuesta * 5)
        print(f"Haz ganado, ahora su monto es de {billetera} pesos")
    else:
        print(f"Haz perdido, ahora su monto es de {billetera} pesos")
    return billetera

billetera = int(input("Ingrese cuanto dinero va a llevar: "))
billetera = juego(billetera)
seguir = True
i = int(input("Desea seguir jugando? (1-si/2-no): "))
if i != 1:
    seguir = False
while seguir == True:
    billetera = juego(billetera)
    i = int(input("Desea seguir jugando? (1-si/2-no): "))
    if i != 1:
        seguir = False