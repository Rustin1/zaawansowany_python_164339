class Square:
    """ Klasa do obsługi figury typu kwadrat"""

    def __init__(self, side=1):
        self.side = side

    def __str__(self) -> str:
        return f"Square({self.side})"

    # tu możemy się zastanowić jak zrealizować dodawanie dwóch kwadratów
    # czy sumujemy długość boku (stworzymy kwadrat o boku, który opisuje dwa kwadraty?, czy też sumujemy pole i wyznaczamy nową wartość size?
    # przyjmijmy ten drugi scenariusz
    # nazwa pierwszego argumenty metody, która w dokumentacji zawsze nosi nazwę self, jest tylko umową, ale wymogiem jest to, że będzie przekazywana
    # do metody zawsze jako pierwszy argument. Więc jak wolimy this to ...
    def __add__(this, other):
        import math
        if isinstance(other, type(this)):
            new_side = math.sqrt(this.side ** 2 + other.side ** 2)
            return type(this)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(this).__name__}' and '{type(other).__name__}'"
            )

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        if isinstance(other, Square):
            # lub
            # if isinstance(other, type(self)):
            return self.side == other.side
        return False


if __name__ == '__main__':
    s = Square(2)
    s2 = Square(3)

    print(s, ' + ', s2, ' to ', s + s2)
    print(s * 3)
    print(s / 2)
    print(s == s2)