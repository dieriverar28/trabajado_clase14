
from os import system
from msvcrt import getch

personas=[]



while True:
    try:
        print('Presione tecla')
        getch()
        system('cls')

        print('''
        ********************************
              sistema registro 
        ********************************
            1) Agregar Persona
            2) Ver Persona
            0) Salir
        ********************************''')
        opcion=int(input('Seleccione : '))

        match opcion:
            case 0:
                break
            case 1:
                if len(personas) >= 10:
                    print('Solo se puede agregar un maximo de 10 personas')
                else:
                    print('Agregar personas')
                    nombre = input('Ingrese nombre : ').capitalize()
                    if nombre not in personas and len(nombre.strip()) > 0:
                        personas.append(nombre)
                        print('persona agregada')
                    else:
                        print('nombre ya registrado')
            case 2:
                if len(personas)>0:
                    print('Ver Personas')
                    for i in range(len(personas)):
                        print(f'{i+1} - {personas[i]}')
                else:
                    print('No hay personas registradas')

               
                
                        


    except Exception as e:
        print(e)
