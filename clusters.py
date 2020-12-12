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
        return([self._x , self._y, self._id])
    
    def get_coord_polar (self):
        self._radio = ((self._x)**2+(self._y)**2)**0.5
        try:
            self._teta = math.atan(self._y/self._x)
        except:
            self._teta = 0
        return([self._radio , self._teta, self._id])

#-------------------------------------------------------------------------------------------------------

def measure_distances(dot_a , dot_b):
    return ((((dot_a[0]-dot_b[0])**2)+((dot_a[1]-dot_b[1])**2))**0.5)

#-------------------------------------------------------------------------------------------------------

def relative_distances(dots):
    dif=[]
    for dot1 in range(len(dots)):
            x1,y1,id1=dots[dot1].get_coord_polar()
            for dot2 in range(len(dots)):
                x2,y2,id2=dots[dot2].get_coord_polar()
                if id1<id2:
                    dif.append([measure_distances([x1,y1],[x2,y2]),id1,id2,])
    dif.sort()
    for iteration in range(len(dif)):
        print(dif[iteration])
    return(dif)
            

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


    dots,x_values,y_values = masive_data(quantity, x_max, y_max)
    relative_distances(dots)

    '''
    print (f"ID 1 = ", dots[ID1].get_coord())
    print (f"ID 2 = ", dots[ID2].get_coord())
    print (f"Distance = ", measure_distances( dots[ID1].get_coord(), dots[ID2].get_coord()))
    '''

    plot(x_values, y_values)


if __name__ == "__main__":
    main()