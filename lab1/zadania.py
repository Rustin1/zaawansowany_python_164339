from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_circumference(self):
        pass

    def __lt__(self, other):
        if isinstance(other, Figure):
            return self.get_area() < other.get_area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Figure):
            return self.get_area() > other.get_area()
        return NotImplemented


class Square(Figure):
    """ Klasa do obsługi figury typu kwadrat """

    def __init__(self, side=1):
        self.side = side

    def __str__(self) -> str:
        return f"Square({self.side})"

    def __add__(self, other):
        if isinstance(other, (Square, int)):
            new_side = math.sqrt(self.side ** 2 + (other.side ** 2 if isinstance(other, Square) else other ** 2))
            return Square(new_side)
        raise TypeError("unsupported operand type for +")

    def __radd__(self, other):
        if isinstance(other, int):
            return self + other
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, (Square, int)):
            self.side = math.sqrt(self.side ** 2 + (other.side ** 2 if isinstance(other, Square) else other ** 2))
            return self
        raise TypeError("unsupported operand type for +=")

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        return isinstance(other, Square) and self.side == other.side

    def get_area(self):
        return self.side ** 2

    def get_circumference(self):
        return 4 * self.side


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius


class Field:

    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, value):
        if name == "value":
            if isinstance(value, int) and 10 <= value <= 2000:
                super().__setattr__(name, value)
            elif isinstance(value, str):
                super().__setattr__(name, value)
            else:
                raise TypeError("value must be an int (10-2000) or str")
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Field({self.value})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Field) and self.value == other.value


if __name__ == '__main__':
    s1 = Square(3)
    s2 = Square(4)
    print(s1 + s2)
    print(s1 + 2)
    print(2 + s1)
    s1 += s2
    print(s1)

    c1 = Circle(5)
    print(f"Circle area: {c1.get_area()}")
    print(f"Circle circumference: {c1.get_circumference()}")

    print(f"Square area: {s1.get_area()}")
    print(f"Square circumference: {s1.get_circumference()}")

    print(s1 > c1)
    print(s1 < c1)

    f1 = Field(100)
    print(f1)
    f1.value = "Bankrut"
    print(f1)

    try:
        f1.value = 5  # Powinien zgłosić wyjątek
    except TypeError as e:
        print(e)
