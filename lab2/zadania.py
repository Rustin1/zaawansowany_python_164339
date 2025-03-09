import csv
from collections import namedtuple
from dataclasses import make_dataclass

# Zadanie 1: Dynamiczna krotka nazwana Order
def create_namedtuple_from_csv(file_path):
    with open(file_path, encoding='utf8') as f:
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)
        field_names = [header.lower().replace(' ', '_') for header in headers]
        Order = namedtuple('Order', field_names)
        orders = [Order._make(row) for row in reader]
    return Order, orders

Order, orders = create_namedtuple_from_csv("zamowienia.csv")
for order in orders[:10]:
    print(order)

# Zadanie 2: Testowanie krotki Point
Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])
p1 = Point(1, 2)
p2 = Point(3, 4)

# Porównania
print(p1 == p2)  # False
print(p1 < p2)   # True (porównanie leksykograficzne)
print(p1 > p2)   # False

# Operacje arytmetyczne (zawiodą, bo namedtuple nie wspiera arytmetyki bezpośrednio)
try:
    print(p1 + p2)
except TypeError as e:
    print("Error:", e)

# Zadanie 3: Dynamiczna klasa danych


def convert_default_value(value, type_str):
    """ Konwertuje stringowe wartości domyślne na odpowiednie typy """
    if type_str == "int":
        return int(value)
    elif type_str == "float":
        return float(value)
    elif type_str == "bool":
        return value.lower() == "true"  # 'True' → True, 'False' → False
    elif type_str == "str":
        return value  # Stringi pozostają bez zmian
    return value  # Jeśli typ jest nieznany, zwracamy oryginalną wartość


def create_dataclass_from_dict(data):
    classes = {}

    for key, value in data.items():
        class_name = value['class_name']
        fields = []

        for field in value['props']:
            name, type_str = field[:2]
            default = field[2] if len(field) == 3 else None

            # Zamiana stringowej nazwy typu na rzeczywisty typ
            type_ = eval(type_str)  # np. 'str' → str

            # Konwersja wartości domyślnej
            if default is not None:
                default = convert_default_value(default, type_str)

            # Tworzenie pola
            if default is not None:
                fields.append((name, type_, default))
            else:
                fields.append((name, type_))

        # Tworzymy klasę dataclass i zapisujemy w słowniku
        classes[class_name] = make_dataclass(class_name, fields)

    return classes


# Testowanie kodu
slownik = {
    1: {
        'class_name': 'Osoba',
        'props': [('name', 'str'), ('is_admin', 'bool', 'False')]
    },
    2: {
        'class_name': 'Produkt',
        'props': [('name', 'str'), ('price', 'float', '0.0'), ('quantity', 'int', '0')]
    }
}

classes = create_dataclass_from_dict(slownik)

# Tworzenie instancji dynamicznie utworzonej klasy
osoba = classes['Osoba'](name="Jan", is_admin=True)
produkt = classes['Produkt'](name="Telefon", price=1999.99, quantity=10)

print(osoba)
print(produkt)