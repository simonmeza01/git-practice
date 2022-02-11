db = { 'Profesores': { "10777124": {'Name': 'Luis', 'LastName': 'Bello', 'Materias': {}}, '11666123' : {'Name': 'Antonio', 'LastName': 'Guerra', 'Materias' : {'FBTSP05': {'Name': 'Algoritmos', 'Creditos': 3}}}}, 'Students': {'28013672': {'Name': 'Rommel', 'LastName': ' Sansonetti', 'Materias': ['Mate5', 'Fisica']}}}
#print(db['Students']['28013672']['Name'])
#el value es el diccionario que hay despues de la cedula de estdiantes por lo tanto ese value ahora es un diccionario
#for key, value in db['Students'].items(): 
#primera forma de hacerlo
#    for key2, value2 in value.items():
#        print(key2, value2)
#    print(f'''Nombre:{value['Name']} 
#Apellido: {value['LastName']}
#''')
#    for materia in value['Materias']:
#        print(materia)
#si quiero imprimir la cedula imprimo el key
for key, value in db['Profesores'].items():
    print(f'''Cedula{key} ,\n Nombre:{value['Name']} , \n Apellido: {value['LastName']}''')
    for key2, value2 in value["Materias"].items():
        print(f'''Codigo{key2}, \n Nombre de la materia: {value2['Name']}, \n Creditos: {value2['Creditos']}''')