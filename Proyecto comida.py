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



niño=(input("¿Es niño? 's' para indicar que si es:"))
if niño =="s":
    edad=int(input("Edad: "))
    if edad <5:
        print("postre gratis!!")
    elif (edad>5)and (edad<12):
        print("Bienvenido")
    else:
        print("no es un niño")
elif niño=="no":
    print("no tiene ningun descuento")
    