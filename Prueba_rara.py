import random
import operator

from bokeh.plotting import figure, show
from bokeh.models import LabelSet, ColumnDataSource
from bokeh.palettes import Category20 as palette

def distancia_euclidiana(a, b):
    return (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5

def distancia_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def distancia_chebyshov(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def generar_datos(rango, cantidad):
    datos = []

    for i in range(cantidad):
        datos.append((random.randint(0, rango), random.randint(0, rango)))
 
    return datos

def par_mas_cercano(centros, tipo):
    n = len(centros)
    distancias = {}

    for i in range(n):
        for j in range(n-i-1):
            if tipo == 1:
                distancia = distancia_euclidiana(centros[i], centros[i + j + 1])
            elif tipo == 2:
                distancia = distancia_manhattan(centros[i], centros[i + j + 1])
            else:
                distancia = distancia_chebyshov(centros[i], centros[i + j + 1])

            distancias[(centros[i], centros[i + j + 1])] = distancia
    
    distancias_sorted = sorted(distancias.items(), key = operator.itemgetter(1))

    par_cercano = distancias_sorted[0][0]

    return par_cercano, distancias_sorted[0][1]

def agrupar(datos, tipo):
    
    clusters_dict = dict(zip(datos, range(len(datos))))

    x = []
    y = []
    names = []

    for coordenada in datos:
        x.append(coordenada[0])
        y.append(coordenada[1])
        names.append(str(datos.index(coordenada)))

    grafica = figure(title = 'Datos', x_axis_label = 'x', y_axis_label = 'y')
    grafica.circle(x, y)

    source = ColumnDataSource(data=dict(x=x, y=y, names=names))
    labels = LabelSet(x='x', y='y', text='names', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')

    grafica.add_layout(labels)

    radio = 0.0

    while len(clusters_dict) > 0:

        print(f'\nClusters {len(datos) - len(clusters_dict) + 1} -> {clusters_dict}')

        centros = []

        for key in clusters_dict.keys():
            centros.append(key)

        if len(clusters_dict) > 1:
            par = par_mas_cercano(centros, tipo)

            print(f'Centros más cercanos -> {par[1]}')

            if type(clusters_dict[par[0][0]]) == int and type(clusters_dict[par[0][1]]) == int:
                new_value = (clusters_dict[par[0][0]], clusters_dict[par[0][1]])
            elif type(clusters_dict[par[0][0]]) == tuple and type(clusters_dict[par[0][1]]) == int:
                new_value = clusters_dict[par[0][0]] + (clusters_dict[par[0][1]],)
            elif type(clusters_dict[par[0][0]]) == int and type(clusters_dict[par[0][1]]) == tuple:
                new_value = (clusters_dict[par[0][0]],) + clusters_dict[par[0][1]]
            else:
                new_value = clusters_dict[par[0][0]] + clusters_dict[par[0][1]]
            
            x_tot = 0
            y_tot = 0

            for k in new_value:
                x_tot += datos[k][0]
                y_tot += datos[k][1]

            x_c = x_tot / len(new_value)
            y_c = y_tot / len(new_value)

            new_centro = (x_c, y_c)

            clusters_dict.pop(par[0][0])
            clusters_dict.pop(par[0][1])
            clusters_dict[new_centro] = new_value
            radio = par[1]

            grafica.circle(new_centro[0], new_centro[1], radius= radio, color = palette[11][(len(datos) - len(clusters_dict)) % len(palette[11])], fill_alpha = 0.1)
        
        else:
            break

    show(grafica)

if __name__ == "__main__":
    rango = int(input('Ingrese el rango de datos: '))
    cantidad = int(input('\nIngrese la cantidad de puntos: '))

    tipo_distancia = int(input('\nSeleccione el tipo de medicion: \n[1] = Euclidiana\n[2] = Manhattan\n[3] = Chebyshov\n\nSeleccion: '))

    datos = generar_datos(rango, cantidad)

    print(f'\nDatos iniciales: {datos}')

    agrupar(datos, tipo_distancia)