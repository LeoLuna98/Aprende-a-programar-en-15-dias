cuarentena = 15
dia = int(input('Ingrese dia: '))
restantes = cuarentena - dia

#Multiway Condition
if restantes > 5:
    print('Quedate en casa. Faltan ',restantes,' dias.')
elif restantes > 0:
    print('Quedate en casa. Faltan poco. Solo quedan ',restantes,' dias.')
else:
    print('Termino la cuarentena.')