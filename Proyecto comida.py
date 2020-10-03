#

# Monto a pagar de lo consumido en el restaurante
monto=float(input("monto a pagar: $"))
cliente=input("¿usted es cliente?'s' para indicar 'si':")#preguntar si es cliente
if cliente=="s":
    descuento=int(input("porcentaje de descuento:"))#hacer descuento si es cliente
    monto=monto-((descuento/100)*monto)
elif 1500<= monto: #Cualquier persona que consuma una cantidad de $1500 o mas, se le hara el 15% de descuento
    descuento_consumo=monto*0.15
    monto=monto-descuento_consumo

print("monto a pagar: $",monto)


#Hacer registro de las personas que entran en grupo
registro=int(input("personas ingresadas:"))
if registro>=10: #si son mas de 10 personas, habra regalos
    print("regalos para ustedes")



niño=(input("¿Es niño? 's' para indicar que si es:"))  #si las personas vienen con niños, se les preguntara
if niño =="s":                                           #la edad, si los niños son menores a 6 años ellos tendran
    edad=int(input("Edad: "))                            #postre gratis!!
    if edad <6:
        print("postre gratis!!")
    elif (edad>5)and (edad<12):
        print("Bienvenido")
    else:
        print("no es un niño")
elif niño=="no":
    print("no tiene ningun descuento")
    
#Para otorgar un estimulo en las personas, cada semana los dias sabados, se estara registrando con numero del 1 al 9
    #el conjunto de personas que entre. (si una familia entra despues de las 12pm sera registrado como el num 1)
aumento_100=[
    [1,2,3],
    [4,5,6],
    [7,8,9],  #Estos son los conjuntos que alcanzaron a entrar en el sorteo; que consiste en aumentar 100 gramos su platillo
    [5]
]

for fila in aumento_100:
    for col in fila:
        print (col)
print("El 5 es el ganador")  # el quinto conjunto sera siempre el establecido para ganar..El aumento de proporcion
                              # en su comida:)
    