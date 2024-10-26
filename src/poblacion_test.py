from poblacion import *
if __name__=='__main__':
    ruta='data/population.csv'
    listatuplas=lee_poblaciones(ruta)
    # print("se han leido", len(listatuplas), "elementos")
    # print(listatuplas)
    # print(calcula_paises(listatuplas))
    # print(filtra_por_pais(listatuplas, 'Arab World'))
    conjunto={'Caribbean Small'}
    print(filtra_por_paises_y_anyo(listatuplas, 1997, conjunto))