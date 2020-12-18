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
    final_list=[]
    final_dif=[]

    for dot1 in range(len(dots)):
            x1,y1,id1=dots[dot1].get_coord()
            for dot2 in range(len(dots)):
                x2,y2,id2=dots[dot2].get_coord()
                if id1<id2:
                    dif.append([measure_distances([x1,y1],[x2,y2]),id1,id2,])
    dif.sort()
    for dis in range(len(dif)):
        _,id_first,id_second=dif[dis]
        if(id_first in final_list or id_second in final_list):pass
            #print("repetido")
        else:
            final_list.append(id_first)
            final_list.append(id_second)
            final_dif.append(dif[dis])

    print(len(final_dif))
    return(final_dif)
            

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

def combine_dots(list_distances,dots):
    new_dots = []
    new_x_values = []
    new_y_values = []
    for id in range(len(list_distances)):
        _,id1,id2=list_distances[id]
        x1,y1,_=dots[id1].get_coord()
        x2,y2,_=dots[id2].get_coord()

        x=(x1+x2)/2
        y=(y1+y2)/2

        new_dots.append(id)
        new_dots[id] = Dato(x,y,id)

        new_x_values.append(x)
        new_y_values.append(y)

    length=len(list_distances)
    if length == 1:pass
    elif length % 2 != 0:
        new_dots.append(0)
        x,y,_=dots[length].get_coord()
        new_dots[length] = Dato(x,y,length)

    return new_dots,new_x_values,new_y_values

#-------------------------------------------------------------------------------------------------------

def plot(x_values, y_values):
    grafica = figure(title= "iteration")
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
    list_distances=relative_distances(dots)
    plot(x_values, y_values)
    while(len(dots) != 1):
        try:
            _ = input('continuar:')
        except ValueError:
            pass

        dots,x_values,y_values=combine_dots(list_distances,dots)
        list_distances=relative_distances(dots)
        plot(x_values, y_values)


if __name__ == "__main__":
    main()