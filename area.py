"""There is a circle inscribed in a square such that all sides touch the circumference of the circle. Write a program to calculate the area inside the square excluding the
 circle if the size of the square is given as an input"""


def area_of_square(size):
    area_square = size * size
    return area_square


def area_of_circle(size):
    area_circle = 3.14 * (size/2) * (size/2)
    return area_circle


if __name__ == '__main__':
    size = int(input('Enter the length of the side of square: '))
    area_exculed_circle = area_of_square(size=size) - area_of_circle(size=size)
    print(area_exculed_circle)