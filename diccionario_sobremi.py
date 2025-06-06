


yo= {
    'primnombre':'Diego',
    'appaterno':'Rivera',
    'fecha_nacim':{
        'dia':3,
        'mes':6,
        'anio':1996
    },
    'signo':'♍',
    'nacion':'Chilena',
    'rut':194738225,
    'edad':28

}
gustos={
    'musica':'De todo 🫦',
    'estudio':'Administracion/Analista Programador',
    'juegosfav':{
        'play':'Crash Bandicoot',
        'nint':'Super Mario',
        'pc':'Alice Madness Returns',
        'pc1':'Half Life'
    },
    'estadociv':'pololeando',
    'perritosfav':{
        'perritos':'Bruno',
        'perrito1':'Pucca',

    },
    'comidasfav':{
        'plato1':'Fideos con salsa y vienesa picada',
        'plato2':'Arroz con chuleta',
        'plato3':'Ramen',
        'plato4':'Teokboki Frito con Salsa agridulce',
        'plato5':'Fideos Camote con pollo'
    }

}


masotros={
    'hobbies':{
        'hobbi1':'Bicicleta',
        'hobbi2':'Raves',
    }
    
}



#mostar ficha



print(f'''
********************************
       {yo['primnombre']} {yo["appaterno"]} {yo["signo"]}  
********************************
Fecha de nacimiento : {yo['fecha_nacim']['dia']} - {yo["fecha_nacim"]['mes']} - {yo["fecha_nacim"]['anio']}
Nacionalidad : {yo["nacion"]}
RUT : {yo["rut"]}
Estado Civil : {gustos["estadociv"]}
Edad : {yo['edad']}''') 
print(f'''
********************************
        OTROS DATOS
********************************
Musica : {gustos["musica"]}
Estudios : {gustos["estudio"]}
Juegos Favoritos : {gustos["juegosfav"]['play']} - {gustos["juegosfav"]['nint']} - {gustos["juegosfav"]['pc']} - {gustos["juegosfav"]['pc1']}
Comidas Favoritas : {gustos["comidasfav"]['plato1']} - {gustos["comidasfav"]['plato2']} - {gustos["comidasfav"]['plato3']} -
{gustos["comidasfav"]['plato4']} - {gustos["comidasfav"]['plato5']} 
Hobbies : {masotros["hobbies"]['hobbi1']} - {masotros["hobbies"]['hobbi2']}
Mis Perritos : {gustos["perritosfav"]['perritos']} y {gustos["perritosfav"]['perrito1']}
''')