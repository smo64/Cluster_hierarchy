<<<<<<< HEAD
import random
from bokeh.plotting import figure, show

class Dato:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def get_coord (self):
        print([self.x , self.y])


#-------------------------------------------------------------------------------------------------------

def masive_data(quantity, x_max, y_max):

    dots = []
    x_values = []
    y_values = []

    for id in range(quantity):
        x = random.randrange(x_max+1)
        y = random.randrange(y_max+1)
        dots.append(id)
        dots[id] = Dato(x,y,id)

        x_values.append(x)
        y_values.append(y)

    return dots,x_values,y_values

#-------------------------------------------------------------------------------------------------------
def plot(x_values, y_values):

    grafica = figure(title= 'Cluster hierarchy')

    grafica.circle(x= x_values, y= y_values, size=10)
    
    show(grafica)
#-------------------------------------------------------------------------------------------------------

def main():

    try:
        x_max = int(input('Ingrese tamaño del eje x:'))
    except ValueError:
        print("10")
        x_max = 10
    try:
        y_max = int(input('Ingrese tamaño del eje y:'))
    except ValueError:
        print("10")
        y_max = 10
    try:
        quantity = int(input('Ingrese la cantidad de puntos a generar:'))
    except ValueError:
        print("10")
        quantity = 10
    try:
        ID = int(input('Ingrese el ID:'))
    except ValueError:
        print("0")
        ID = 0


    dots,x_values,y_values = masive_data(quantity, x_max, y_max)
    plot(x_values, y_values)

    dots[ID].get_coord()

if __name__ == "__main__":
=======
import random
from bokeh.plotting import figure, show

dots = []

class Dato:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

#-------------------------------------------------------------------------------------------------------

def get_coord (dato):
        
        for dot in dots:
            if dot.id == dato:
                break
            else:
                pass

        return dot.x, dot.y

#-------------------------------------------------------------------------------------------------------

def masive_data(quantity, x_max, y_max):

    x_values = []
    y_values = []

    for i in range(quantity):
        x = random.randrange(x_max+1)
        y = random.randrange(y_max+1)
        dot = Dato(x, y, i)

        dots.append(dot)
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

#-------------------------------------------------------------------------------------------------------
def plot(x_values, y_values, x1, y1, x2, y2, distancia):

    Texto = "Distancia= " + str(distancia) 
    grafica = figure(title= 'Cluster hierarchy')

    grafica.circle(x= x_values, y= y_values, size=10)
    grafica.line(x = [x1 , x2], y = [y1, y2], color = "red", legend_label = Texto)
    
    show(grafica)
#------------------------------------------------------------------------------------------------------

def dist_measure(id1, id2):
        x1, y1 = get_coord(id1)
        x2, y2 = get_coord(id2)

        distancia = (((x1 - x2)**2)+((y1 - y2)**2))**0.5

        return distancia, x1, y1, x2, y2

#-------------------------------------------------------------------------------------------------------


def main():

    try:
        x_max = int(input('Ingrese tamaño del eje x (por defecto = 10):'))
    except ValueError:
        x_max = 10
    try:
        y_max = int(input('Ingrese tamaño del eje y (por defecto = 10):'))
    except ValueError:
        y_max = 10
    try:
        quantity = int(input('Ingrese la cantidad de puntos a generar (por defecto = 10):'))
    except ValueError:
        quantity = 10

    x_values, y_values = masive_data(quantity, x_max, y_max)

    id1 = int(input('valor 1: '))
    id2 = int(input('valor 2: '))

    print (get_coord(id1), get_coord(id2))

    distancia, x1, y1, x2, y2 = dist_measure(id1, id2)
    print (distancia)
    plot(x_values, y_values, x1, y1, x2, y2, distancia)


if __name__ == "__main__":
>>>>>>> 157f837d493f446424effb47b0be746e47321669
    main()