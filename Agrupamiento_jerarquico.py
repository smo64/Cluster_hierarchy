import random

def random_generate(max_x, max_y, quantity):
    dots = []

    for _ in range(quantity):
        x_cord = random.randrange(max_x+1)
        y_cord = random.randrange(max_y+1)
        dot = (x_cord, y_cord)

        dots.append(dot)
        
    print (dots)
    return dots



if __name__ == "__main__":
    max_x = int(input("tamaño del eje x:"))
    max_y = int(input("tamaño del eje y:"))
    quantity = int(input("cuantos puntos desea agregar?:"))

    random_generate(max_x, max_y, quantity)


