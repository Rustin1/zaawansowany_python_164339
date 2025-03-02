class Dummy():
    # a to poniżej to docstring
    """ Testowy obiekt """

    # zmienna klasowa - współdzielona pomiędzy instancje klasy Dummy
    class_counter = 0

    # inicjalizator
    def __init__(self):
        print("__init__()")
        # dostęp do zmiennej klasowej odbywa się jak poniżej
        Dummy.class_counter += 1
        # zmienna instancji
        self.foo = 'foo foo'

    # metoda new() jest wywoływana przed inicjalizatorem
    # i zwraca obiekt wywoływanego typu (czyli tu Dummy)
    # można to nazwać konstruktorem
    def __new__(cls, *args, **kwargs):
        print('__new__()')
        return super().__new__(cls)

    # metoda del jest wywoływana w momencie usuwania obiektu z pamięci
    # czyli w momencie "śmierci" obiektu (spadek liczby referencji do 0 do obszaru
    # w pamięci zajmowanego przez obiekt), nazywana destruktorem
    def __del__(self):
        print('__del__()')


d = Dummy()
print(d.__doc__)
print(d.class_counter)
print(d.foo)

# zmienna obiektu
d.so_what = 'Who am I?'

print(d.__dict__)

del d

d1 = Dummy()
print(d1.class_counter)
print(d1.foo)
print(d1.__dict__)
#
# Testowy obiekt
# 1
# foo foo
# {'foo': 'foo foo', 'so_what': 'Who am I?'}
# __del__()
# __new__()
# __init__()
# __del__()
# 2
# foo foo
# {'foo': 'foo foo'}
#
