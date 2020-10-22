import random  # Para obtener un numero aleatorio

""" Este programa lo que realiza es que facilita el manejo en un restaurante,
    al tener las operaciones al instante, como son los porcentajes de
    descuento, los montos que una persona obtuvo, los obsequios que se dan,
    los paquetes que hay; agiliza los procesos.

    Creado por: Karla Karolina Gortares Gaxiola
    Matricula: A01703813
    Materia: Pensamiento computacional
"""


"""
================== Biblioteca  =====================================
"""

""" Ahora se daran una lista de precios de los
    paquetes que hay en el menu
"""

print ("Paquetes del menu")
menu = [300, 250, 320, 230, 100, 250, 410, 120]
for pos in range(len(menu)):
    print ("Paquete", pos, "cuesta", menu[pos])


""" Monto a pagar de lo consumido en el restaurante_
    Preguntar si es cliente_
    Hacer descuento si es cliente_
    Cualquier persona que consuma una cantidad de $1500 o
    mas, se le hara el 10% de descuento
"""
monto = float(input("monto a pagar: $"))
cliente = input("¿usted es cliente?'s' para indicar 'si':")
if cliente == "s":
    descuento = int(input("porcentaje de descuento:"))
    monto = monto-((descuento/100)*monto)
elif 1500 <= monto:
    descuento_consumo = monto*0.10
    monto = monto-descuento_consumo

print ("monto a pagar: $", monto)

"""
================== Función  =====================================
"""
# promedio de clientes en la semana
def promedio(semana):
    acum = 0.0
    for elem in semana:
        acum = acum+elem
    return acum/len(semana)
print (promedio([73, 97, 125, 115, 120, 92, 82]))


""" Hacer registro de las personas que entran en grupo
    si son mas de 16 personas, habra regalos
"""
registro = int(input("personas ingresadas:"))
if registro >= 16:
    print ("regalos para ustedes")

""" si las personas vienen con niños, se les preguntara
    la edad, si los niños son menores a 6 años ellos tendran
    postre gratis!!
"""
niño = (input("¿Es niño? 's' para indicar que si es:"))
if niño == "s":
    edad = int(input("Edad: "))
    if edad < 6:
        print ("postre gratis!!")
    elif (edad > 5) and (edad < 12):
        print ("Bienvenido")
    else:
        print ("no es un niño")
elif niño == "no":
    print ("no tiene ningun descuento")


""" Habra rifa cada semana se estara registrando
    con numero del 1 al 9 el conjunto de personas
    que entre. (si una familia entra despues de las
    12pm sera registrado como el num 1, en el sorteo de aumento en
    100gr tu comida) sorteo Random, utilizando biblioteca extra
"""
print ("Ahora se realizará una rifa")
aumento_100 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

familia_ganadora = random.choice(aumento_100)  # se obtiene un numero aleatorio
numero_ganador = random.choice(familia_ganadora)  # ganador aleatoriamente
print ("El numero ganador es", numero_ganador)

