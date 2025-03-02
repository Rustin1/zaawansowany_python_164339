# sposób 1 - wyrzucanie wyjątku NotImplementedError

class Figure:

    def __init__(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")
    def get_field(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")

class CircleEmpty(Figure):
    pass

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

if __name__ == "__main__":
    c = Circle(5)
    c2 = CircleEmpty()


    # sposób 2 - użycie instrukcji assert

    class Figure:

        def __init__(self):
            assert False, "Należy zaimplementować tę metodę"

        def get_field(self):
            assert False, "Należy zaimplementować tę metodę"


    class CircleEmpty(Figure):
        pass


    class Circle(Figure):

        def __init__(self, radius):
            self.radius = radius


    if __name__ == "__main__":
        c = Circle(5)
        c2 = CircleEmpty()

        # sposób 3 - z użyciem klas ABC (Abstract Base Classes) - tutaj tylko prosty przykład, bardziej szczegółowo
        # klasami ABC zajmiemy się na kolejnych laboratoriach
        from abc import ABCMeta, abstractmethod


        class Figure(metaclass=ABCMeta):

            @abstractmethod
            def __init__(self): pass

            @abstractmethod
            def get_field(self): ...


        class CircleEmpty(Figure):
            pass


        class Circle(Figure):

            def __init__(self, radius):
                self.radius = radius

            def get_field(self):
                import math
                return (math.PI * self.radius) ** 2


        if __name__ == "__main__":
            c = Circle(5)
            c2 = CircleEmpty()