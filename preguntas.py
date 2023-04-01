"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.
"""
def Datos():
    Data = open('data.csv', 'r').readlines()
    Data = [z.replace("\n", "") for z in Data]# se remplaza el salto de linea por vacío ""
    Data = [z.split("\t") for z in Data]#se divine la cadena en cada tab ("\t")
    return Data

Datos()



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    Columna2 = [z[1] for z in Datos()[0:]]

    Suma = 0
    for i in Columna2:
        Suma += int(i)
    
    return Suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    import string
    Columna1 = [z[0] for z in Datos()[0:]]

    Contador_de_letras = {letra:0 for letra in string.ascii_lowercase}

    for lista in Columna1:
        for elemento in lista:
            if elemento.isalpha():
                letra = elemento.lower()
                Contador_de_letras[letra] +=1

    lista_tuplas = sorted(Contador_de_letras.items())
    lista_tuplas_filtrada =[tupla for tupla in lista_tuplas if not 0 in tupla]
    lista_tuplas_mayuscula = list(map(lambda tupla: (tupla[0].upper() if isinstance(tupla[0], str) else tupla[0], tupla[1]), lista_tuplas_filtrada))
    return lista_tuplas_mayuscula


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    Tabla1 = sorted([z[:2] for z in Datos()])
    Columna1 = [z[0] for z in Datos()[0:]]
    Grupos = sorted(list(set(Columna1)))

    Suma = 0
    ListaSuma = []

    for i in Grupos:
        Suma = 0
        for j in Tabla1:    
            if i[0] == j[0]:
                Suma += int(j[1])
        ListaSuma.append(Suma)
    Lista_Tuplas = sorted(list(zip(Grupos, ListaSuma)))


    return Lista_Tuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    #Ejercicio 4
    Columna3 = [z[2] for z in Datos()[0:]]
    Campos_Fechas = [z.split("-") for z in Columna3]
    Columna_Mes = [z[1] for z in Campos_Fechas]

    Grupos = list(set(Columna_Mes))
    Lista_Conteo = []

    for i in Grupos:
        Conteo = Columna_Mes.count(i)
        Lista_Conteo.append(Conteo)
    Lista_Tuplas = sorted(list(zip(Grupos, Lista_Conteo)))
    
    return Lista_Tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    diccionario = {}
    for i in Datos():
        if i[0] in diccionario.keys():
            diccionario[i[0]].append(int(i[1]))
        else:
            diccionario[i[0]] = [int(i[1])]

    resultado = [(a,max(diccionario[a]),min(diccionario[a])) for a in diccionario.keys()]
    resultado = sorted(resultado, key=lambda tup: tup[0])

    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """    
    lista = []
    for a in [i[4].split(',') for i in Datos()]:
        lista.extend(a)
        diccionario = {}
        for b in lista:
            clave = b.split(':')[0]
            valor = b.split(':')[1]
            if clave in diccionario.keys():
                diccionario[clave].append(int(valor))
            else:
                diccionario[clave] = [int(valor)]
    
    resultado = [(clave, min(diccionario[clave]), max(diccionario[clave])) for clave in diccionario.keys()]
    sorted(resultado, key=lambda tup: tup[0])

    return sorted(resultado, key=lambda tup: tup[0])



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """  
    diccionario = {}
    for i in Datos():
        clave = int(i[1]) 
        if clave in diccionario.keys():
            diccionario[clave].append(i[0])
        else:
            diccionario[clave] = [i[0]]

    lista = list(diccionario.items())
    
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """ 
    diccionario = {}
    for i in Datos():
        clave = int(i[1])
        if clave in diccionario.keys():
            diccionario[clave].append(i[0])
        else: 
            diccionario[clave] = [i[0]]
    
    resultado = sorted(list(diccionario.items()))
    resultado = [(b[0], sorted(list(set(b[1])))) for b in resultado]
    
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista = []

    for a in [i[4].split(',') for i in Datos()]:
        lista.extend(a)

    diccionario = {}

    for b in sorted(lista):
        clave = b.split(':')[0]
        valor = b.split(':')[1]
        if clave in diccionario.keys():
            diccionario[clave] = diccionario[clave] + 1
        else:
            diccionario[clave] = 1

    resultado = dict(list(diccionario.items()))

    return resultado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista = []
    for i in Datos():
        lista.append((i[0], len(i[3].split(',')),len(i[4].split(','))))

    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    diccionario = {}
    for i in Datos():
        for a in i[3].split(','):
            if a in diccionario.keys():
               diccionario[a] = diccionario[a] + int(i[1])
            else:
                diccionario[a] = int(i[1])
    
    resultado = list(diccionario.items())

    return dict(sorted(resultado, key=lambda tup: tup[0]))
    


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    for i in Datos():
        c = i[4].split(',')
        if i[0] in diccionario.keys():
            diccionario[i[0]] = diccionario[i[0]] + sum([int(e.split(':')[1]) for e in c])
        else:
            diccionario[i[0]] = sum([int(e.split(':')[1]) for e in c])
    resultado = list(diccionario.items())
    resultado = dict(sorted(resultado, key=lambda tup: tup[0]))
    return resultado
    
