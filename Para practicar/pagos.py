gasto = int(input('Ingrese monto gastado: '))

if gasto <= 100:
    print('Pago con efectivo')
elif gasto < 300:
    print('Pago con tarjeta de debito')
else:
    print('Pago con efectivo')