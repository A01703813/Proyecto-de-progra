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
while niño=="s":
    edad=int(input("edad del niño:"))#si hay niños, introducir la edad del niño
    if 1<=edad <= 5:
        print("postre para el niño")#si el niño tiene 5 años ó menos, se le regalará un postre
    elif edad<0:
        print("intentelo de nuevo")
    elif edad >5:
        print("no se encuentra dentro de los requisitos")

    