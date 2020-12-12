import random
import math
from bokeh.plotting import figure, show

class Dato:
    def __init__(self, x, y, id):
        self._x = x
        self._y = y
        self._id = id
        self._radio = None
        self._teta = None

    def get_coord (self):
        return([self._x , self._y])
    
    def get_coord_polar (self):
        self._radio = ((self._x)**2+(self._y)**2)**0.5
        self._teta = math.atan(self._y/self._x)
        return([self._radio , self._teta])

#-------------------------------------------------------------------------------------------------------

def measure_distances(dot_a , dot_b):
    return ((((dot_a[0]-dot_b[0])**2)+((dot_a[1]-dot_b[1])**2))**0.5)

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
def plot(x_values, y_values , dot_a , dot_b):

    grafica = figure(title= 'Cluster hierarchy')
    line_x = [dot_a[0],dot_b[0]]
    line_y = [dot_a[1],dot_b[1]]

    grafica.circle(x= x_values, y= y_values, size=10)
    grafica.line(x=line_x ,y=line_y,color="red")
    
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
        ID1 = int(input('Ingrese el ID 1:'))
    except ValueError:
        print("0")
        ID1 = 0
    try:
        ID2 = int(input('Ingrese el ID 2:'))
    except ValueError:
        print("1")
        ID2 = 1


    dots,x_values,y_values = masive_data(quantity, x_max, y_max)

    print (f"ID 1 = ", dots[ID1].get_coord())
    print (f"ID 2 = ", dots[ID2].get_coord())
    print (f"Distance = ", measure_distances( dots[ID1].get_coord(), dots[ID2].get_coord()))

    plot(x_values, y_values , dots[ID1].get_coord() , dots[ID2].get_coord())


if __name__ == "__main__":
    main()