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
    final_dif=[]
    n=0
    f=0
    for dot1 in range(len(dots)):
            x1,y1,id1=dots[dot1].get_coord()
            for dot2 in range(len(dots)):
                x2,y2,id2=dots[dot2].get_coord()
                if id1<id2:
                    dif.append([measure_distances([x1,y1],[x2,y2]),id1,id2,])
    dif.sort()
    for dis_first in range(len(dif)):
        _,id1,id2=dif[dis_first]
        for dis_second in range(len(dif)):
            _,id3,id4=dif[dis_second]
            if(id1==id3 or id1==id4 or id2==id3 or id2==id4):
                f=f+1
            else:
                n=n+1           
    print(f,n)
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
    while(len(dots)>1):
        try:
            _ = input('continuar:')
        except ValueError:
            pass
        dots,x_values,y_values=combine_dots(list_distances,dots)
        list_distances=relative_distances(dots)
        plot(x_values, y_values)

if __name__ == "__main__":
    main()