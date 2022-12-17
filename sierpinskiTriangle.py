import render
import pygame
import random

# Window dimensions
width = 750
height = 750
window = render.render(False,750,750)
window.setBackgroundColor(window.colors.black)
starting_coordinates = list()

def draw_triangle(window):
    base = random.randint(300,500)
    first_vertex_Y = 600
    first_vertex_X = 50
    second_vertex_Y = 600
    second_vertex_X = first_vertex_X + base
    height = random.randint(300,500)
    third_vertex_X = (first_vertex_X + second_vertex_X)/2
    third_vertex_Y = first_vertex_Y - height
    starting_coordinates.append((int(first_vertex_X),int(first_vertex_Y)))
    starting_coordinates.append((int(second_vertex_X),int(second_vertex_Y)))
    starting_coordinates.append((int(third_vertex_X),int(third_vertex_Y)))
    window.draw_thick_pixel(starting_coordinates[0], window.random_color())
    window.draw_thick_pixel(starting_coordinates[1], window.random_color())
    window.draw_thick_pixel(starting_coordinates[2], window.random_color())
    print("base: " + str(base))
    print("height: " + str(height))
    print("Vertices of triangle: " + str(starting_coordinates))


def get_starting_coordinates():
    while True:
        x = random.randint(0,width - 1)
        y = random.randint(0,height- 1)
        if(are_coordinates_inside_triangle(x,y)):
            return (x,y)

def are_coordinates_inside_triangle(x,y):
    d1 = sign((x,y),starting_coordinates[0],starting_coordinates[1])
    d2 = sign((x,y),starting_coordinates[1],starting_coordinates[2])
    d3 = sign((x,y),starting_coordinates[2],starting_coordinates[0])
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not(has_neg and has_pos)

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p2[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def main():
    draw_triangle(window)
    starting_pixel = get_starting_coordinates()
    window.draw_thick_pixel(starting_pixel, window.random_color())
    current_pixel = starting_pixel
    count = 0

    running = True
    while running:
        current_vertex = starting_coordinates[random.randint(0,2)]
        xm = (current_vertex[0]+current_pixel[0])/2
        ym = (current_vertex[1]+current_pixel[1])/2
        new_coordinates = (int(xm),int(ym))
        window.draw_thick_pixel(new_coordinates, window.random_color())
        current_pixel = new_coordinates
        count += 1
        running = window.check_for_exit()


if __name__ == "__main__":
    main()