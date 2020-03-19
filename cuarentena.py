cuarentena = 15
dia = int(input('Ingrese dia: '))
restantes = cuarentena - dia

#Two Way Condition
if restantes > 0:
    print('Quedate en casa. Faltan ',restantes,' dias.')
else:
    print('Termino la cuarentena.')