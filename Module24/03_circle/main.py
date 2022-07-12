import math


class Circle:

    def __init__(self, coordinate_x=0, coordinate_y=0, radius_circle=1):

        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius_circle = radius_circle

    def perimeter_circle(self):

        perimeter = 2 * math.pi * self.radius_circle
        return perimeter

    def sqear_circle(self):

        sq_circle = math.pi * self.radius_circle ** 2
        return sq_circle

    def growing_circle(self, k):

        self.radius_circle *= k
        return self.radius_circle

    def intersection_of_circles(self, other):

        return (self.coordinate_x - other.coordinate_x) ** 2 + (self.coordinate_y - other.coordinate_y) ** 2\
               <= (self.radius_circle + other.radius_circle) ** 2


# circle_1 = Circle()
# circle_2 = Circle(2, 3, 2)
#
# print(f'Периметр первого круга: {circle_1.perimeter_circle()}')
# print(f'Периметр второго круга: {circle_2.perimeter_circle()}')
# print(f'Площадь первого круга: {circle_1.sqear_circle()}')
# print(f'Площадь второго круга: {circle_2.sqear_circle()}')
# print(f'Радиус первого круга увеличился и составил: {circle_1.growing_circle(3)}')
# print(f'Радиус второго круга увеличился и составил: {circle_2.growing_circle(4)}')
# print(f'Круги пересекаются - {circle_1.intersection_of_circles(circle_2)}')
