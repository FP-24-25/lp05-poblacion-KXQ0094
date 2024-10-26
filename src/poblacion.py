from collections import namedtuple
import csv
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    listapoblacion=[]
    with open(ruta_fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=',')
        for linea in lector:
            año=int(linea[2])
            censo=int(linea[3])
            e=RegistroPoblacion(linea[0], linea[1], año, censo)
            listapoblacion.append(e)
    return listapoblacion

def calcula_paises(poblaciones):
    paiseslista= set()
    for registro in poblaciones:
        paiseslista.add(registro.pais)
    return sorted(paiseslista)
    
def filtra_por_pais(poblaciones, nombre_o_codigo):
    datospais=[]
    for registro in poblaciones:
        if registro.pais==nombre_o_codigo or registro.codigo==nombre_o_codigo:
            datospais.append(registro.año and registro.censo)
    return datospais

def filtra_por_paises_y_anyo(poblaciones, anyo, conjuntonompaises):
    datos=[]
    anyoreal=anyo-1
    for elemento in poblaciones:
        if elemento.pais in conjuntonompaises and elemento.año==anyoreal:
            datos.append(elemento.pais and elemento.censo )
    return datos
