class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        rect = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            rect += (self.width * "*" + "\n") * self.height
        return rect

    def get_amount_inside(self, shape):
        sur = shape.width * shape.height
        return self.get_area() // sur

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


rec = Rectangle(10, 12)
print(rec.get_picture())
