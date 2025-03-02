# implementację wzorca singleton, czyli ograniczenie możliwości tworzenia instancji danego obiektu tylko do 1 sztuki
class DummySingleton():
    """ Testowy obiekt """

    instance = None

    def __init__(self):
        print("__init__()")

    def __new__(cls):
        print('__new__()')
        if DummySingleton.instance is None:
            DummySingleton.instance = object.__new__(cls)

        return DummySingleton.instance

    def __del__(self):
        print('__del__()')


single = DummySingleton()
single.name = "To Singleton"
print(id(single))

single2 = DummySingleton()
print(single2.name)
print(id(single2))