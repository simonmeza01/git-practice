bd = {}
print('Bienvenido')
resp = 's'
while resp == 's':
    menu = input('Ingresa: \n1.Ingreso de estudiante a la basa de datos. \n2.Para eliminar un estudiante de la base de datos. \n3.Para mostrar los estudiantes registrados en la base de datos. \n4. Editar a un estudiante registrado \n==>')
    while not (menu.isnumeric() and 1<= int(menu) <=5):
        menu = input('Ingreso Invalido. Ingresa: \n1.Ingreso de estudiante a la basa de datos. \n2.Para eliminar un estudiante de la base de datos. \n3.Para mostrar los estudiantes registrados en la base de datos.\n4. Para editar un estudiante registrado. \n==>')
    if int(menu) == 1:
        name= input('Ingresa el nombre del estudiante: ')
        while not name.isalpha():
            name= input('Ingreso Invalido.Ingresa el nombre del estudiante: ')
        last_name =input('Ingresa el apellido del estudiante: ')
        while not last_name.isalpha():
            last_name =input('Ingreso Invalido.Ingresa el apellido del estudiante: ')
        dni = input('Ingrese su cedula: ')
        while not dni.isnumeric():
            dni = input('Ingreso Invalido. Ingrese su cedula: ')
        asignaturas = []
        option = 0
        while option == 0:    
            materia = input('Ingresa el nombre de la materia: ')
            while not materia.isalpha():
                materia = input('Ingresa el nombre de la materia: ')
            option = input('Ingres 0 si desea continuar o ingrese 1 si desea salir: ')
            while not((0<=int(option)<= 1) and option.isnumeric()):
                option = input('Ingres 0 si desea continuar o ingrese 1 si desea salir: ')
            asignaturas.append(materia)
            option=int(option)
            bd[dni] = {'name':name , 'lastName':last_name, 'Asignaturas':asignaturas }
    elif int(menu) ==2:
        for key, value in bd.items():
            print(f'''\nCedula {key}\nNombre {value['name']}\nApellido {value['lastName']}''')
            print('Materias:')
            for materia in value['Asignaturas']:
                print(materia)
        dni = input('Ingrese la cedula que desea eliminar: ')
        while not dni == key:
            dni = input('Ingreso Invalido. Ingrese la cedula que desea eliminar: ')
        bd.pop(dni)
    elif int(menu) ==3:
        for key, value in bd.items():
            print(f'''\nCedula {key}\n Nombre: {value['name']}\nApellido {value['lastName']}''')
            print('Materias:')
            for materia in value['Asignaturas']:
                print(materia)
    elif int(menu) ==4:
        for key, value in bd.items():
            print(f'''\nCedula {key}\n Nombre: {value['name']}\nApellido {value['lastName']}''')
            print('Materias:')
            for materia in value['Asignaturas']:
                print(materia)
        dni = input('Ingrese la cedula del estudiantes que deseas editar: ')
        opt =input('Ingresa: \n1. Para cambiar el nombre del estudiante. \n2. Para cambiar el apellido del estudiante. \n3. Para cambiar la cedula del estudiante. \n4. Para cambiar las asignaturas del estudiantes. \n5. Salir')
        while not (opt.isnumeric() and 1<= int(opt)<5):
            opt =input('Ingreso Invalido. Ingresa una de las opciones correspondientes: \n1. Para cambiar el nombre del estudiante. \n2. Para cambiar el apellido del estudiante. \n3. Para cambiar la cedula del estudiante. \n4. Para cambiar las asignaturas del estudiantes.')
        if int(opt) == 1:
            name = input('Ingresa el nombre: ')
            bd[dni]['name'] = name
        elif int(opt) ==2:
            last_name = input('Ingresa el apellido: ')    
            bd[dni]['name'] = last_name
        elif int(opt) ==3:
            dni2 = input('Ingrese la cedula: ')
            student= bd[dni]
            bd[dni2]=student
            bd.pop(dni)
        elif int(opt) ==4:
            option = input('Ingrese una opcion: \n1. Quitar Materia \n2. Agregar Materia')
            if int(option) == 1:
                for index in range(len(bd[dni]['materias'])):
                    print(index+1,bd[dni]['materias'][index] )
                    m = input('Ingrese el numero de la materia que desea borrar: ')
                    bd[dni]['materias'].pop(m-1)
            elif int(option) ==2:
                materia = input('Ingrese el nombre de la materia a agregar: ')
                bd[dni]['materias'].append(materia)
            else:
                print('***Adios***')
        else:
            break
    else:
            print('***ADIOS***')
            break
