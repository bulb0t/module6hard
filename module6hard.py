from math import pi

class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        self.__sides = self.__is_valid_init_sides(sides)
        self. __color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    @classmethod
    def __is_valid_color(cls, *color):
        for c in tuple(color):
            if type(c) != int or c < 0 or c > 255:
                return False
        return True

    def __is_valid_init_sides(self, sides):
        if type(sides) == int and self.sides_count != 1:
            return [sides for _ in range(self.sides_count)]
        elif type(sides) == tuple and self.sides_count < len(sides):
            return [1 for _ in range(self.sides_count)]
        elif type(sides) == tuple and self.sides_count > len(sides):
            return sides[0]
        else:
            return sides

    def set_color(self, *color):
        if not self.__is_valid_color(*color):
            print('Введите другие значения цветов. Число должно входить в диапазон от 0 до 255 включительно и быть '
                  'целым числом. Цвет не был изменён')
        else:
            self.__color[0] = color[0]
            self.__color[1] = color[1]
            self.__color[2] = color[2]


    def __is_valid_sides(self, sides):
        if len(sides) == 1 and self.sides_count != 1:
            return False
        else:
            if self.sides_count != len(sides):
                return False
            else:
                for side in sides:
                    if type(side) != int:
                        return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        sides_count = len(new_sides)
        if self.__is_valid_sides(new_sides):
            if sides_count == self.sides_count:
                self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (pi * 2)


    def get_square(self):
        return 2 * pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        perimeter = sum(self.__sides)
        return (perimeter*(perimeter-self.__sides[0])*(perimeter-self.__sides[1])*(perimeter-self.__sides[2])) ** (1/2)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides for _ in range(12)]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())