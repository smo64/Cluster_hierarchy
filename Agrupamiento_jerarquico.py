import random
from bokeh.plotting import figure, show  

def random_generate(max_x, max_y, quantity):
    dots = []

    for _ in range(quantity):
        x_cord = random.randrange(max_x+1)
        y_cord = random.randrange(max_y+1)
        dot = (x_cord, y_cord)

        dots.append(dot)
        
    print (dots)
    return dots

def plot (x,y):
   # grafica = figure(title='Cluster hierarchy', plot_height = 400, plot_width = 400)
    

if __name__ == "__main__":
    max_x = int(input("tamaño del eje x:"))
    max_y = int(input("tamaño del eje y:"))
    quantity = int(input("cuantos puntos desea agregar?:"))

    random_generate(max_x, max_y, quantity)


