import random
from bokeh.plotting import figure, show

class Dato:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def get_coord (self):
        print([self.x , self.y])
        return([self.x , self.y])

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
    plot(x_values, y_values)

    measure = measure_distances( dots[ID1].get_coord(), dots[ID2].get_coord())
    print (measure)

if __name__ == "__main__":
    main()