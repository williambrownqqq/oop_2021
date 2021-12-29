class Rectangle:
    def __init__(self, length=2, width=1):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width):
        if isinstance(width, float) or 0.0 <= width or width > 20.0:
            self.__width = width
        else:
            raise ValueError("error")

    @length.setter
    def length(self, length):
        if isinstance(length, float) or 0.0 <= length or length > 20:
            self.__length = length
        else:
            raise ValueError("error")

    def per(self):
        return (self.__width + self.__length) * 2

    def area(self):
        return self.__width * self.__length


def main():
    try:
        abc = Rectangle(2, -6)
        print("perimetr = ", abc.per())
        print("area = ", abc.area())
    except ValueError:
        print("error")



main()
