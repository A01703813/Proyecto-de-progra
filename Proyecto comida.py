monto=float(input("monto a pagar: $"))
cliente=input("¿usted es cliente?'s' para indicar 'si':")
if cliente=="s":
    descuento=int(input("porcentaje de descuento:"))
    monto=monto-((descuento/100)*monto)
print("monto a pagar: $",monto)
