class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value
        return self.width

    def set_height(self, value):
        self.height = value
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        x = ''
        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        for i in range(self.height):
            for j in range(self.width):
                x += '*'
            x += '\n'
        return x

    def get_amount_inside(self, other_class):
        x = self.get_area() / other_class.get_area()

        # since we are not allowed to use any library,
        # I made my own method of math.ceil to round
        # number to its lower whole number
        x_str = str(x)
        x_dot = x_str.find('.')
        if x_dot == -1:
            print(x)
        else:
            x = int(x_str[:x_dot])
            print(x)
        return x

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)

    def set_side(self, value):
        if self.set_width(value):
            self.side = self.set_height(value)
        if self.set_height(value):
            self.side = self.set_width(value)
        return value

    def __str__(self):
        return f'Square(side={self.width})'



# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())
#
# sq = Square(5)
# print(sq)
# print(sq.get_area())
#
# print(sq.set_side(4))
# print(sq)
# print(sq.get_area())
# print(sq.get_picture())
#
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))
