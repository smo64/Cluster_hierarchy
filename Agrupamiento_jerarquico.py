import random
from bokeh.plotting import figure, show  

class Dato:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def random_generate(max_x, max_y, quantity):
    dots = []
    x_vector = []
    y_vector = []

    for _ in range(quantity):
        x_cord = random.randrange(max_x+1)
        y_cord = random.randrange(max_y+1)
        dot = (x_cord, y_cord)

        x_vector.append(x_cord)
        y_vector.append(y_cord)
        dots.append(dot)
        
    return dots, x_vector, y_vector

def plot (dots, x_vector, y_vector):
    grafica = figure(title='Cluster hierarchy', plot_height = 400, plot_width = 400)

    grafica.circle(x = x_vector, y = y_vector, size = 10)
    show(grafica)


if __name__ == "__main__":
    max_x = int(input("tamaño del eje x:"))
    max_y = int(input("tamaño del eje y:"))
    quantity = int(input("cuantos puntos desea agregar?:"))

    dots, x_vector, y_vector = random_generate(max_x, max_y, quantity)
    plot(dots, x_vector, y_vector)


