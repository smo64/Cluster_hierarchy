import random
from bokeh.plotting import figure , show , output_file

def random_generate(max_x, max_y, quantity):
    dots = []

    for _ in range(quantity):
        x_cord = random.randrange(max_x+1)
        y_cord = random.randrange(max_y+1)
        dot = (x_cord, y_cord)

        dots.append(dot)
    return dots

def plot (x,y):
   grafica = figure(title='Cluster hierarchy', plot_height = 400, plot_width = 400)
   grafica.circle(x,y,size=10, color="navy", alpha=0.5)
   show(grafica)
    

if __name__ == "__main__":
    max_x = int(input("tamaño del eje x:"))
    max_y = int(input("tamaño del eje y:"))
    quantity = int(input("cuantos puntos desea agregar?:"))
    cord_x = []
    cord_y = []

    dots=random_generate(max_x, max_y, quantity)

    for dot in dots:
        cord_x.append(dot[0])
        cord_y.append(dot[1])

    plot(cord_x,cord_y)