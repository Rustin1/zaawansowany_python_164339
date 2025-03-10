from abc import ABC, abstractmethod
from datetime import date
from collections.abc import MutableSequence, Collection
import inspect


# ------------------------------
# 1. Klasa bazowa Field + Enum FieldType jako klasa wewnętrzna
# ------------------------------
class Field(ABC):
    """ Klasa bazowa dla wszystkich pól modelu """

    class FieldType:
        """ Klasa wewnętrzna Enum definiująca typy pól """
        from enum import Enum

        class Type(Enum):
            INTEGER = 1
            FLOAT = 2
            STRING = 3
            DATE = 4

    def __init__(self):
        self._value = None  # Zmieniamy nazwę zmiennej na `_value`

    def get_fieldtype(self):
        return self.__class__.__name__

    def __setattr__(self, attr, val):
        if attr == 'value':
            self._set_field_value(val)
        else:
            super().__setattr__(attr, val)

    @abstractmethod
    def _get_field_value(self):
        ...

    @abstractmethod
    def _set_field_value(self, val):
        ...

    def __str__(self):
        return str(self._get_field_value())


# ------------------------------
# 2. Implementacja StringField, IntegerField, DateField
# ------------------------------
class StringField(Field):

    def _set_field_value(self, val):
        if isinstance(val, str):
            self._value = val

    def _get_field_value(self):
        return self._value


class IntegerField(Field):

    def _set_field_value(self, val):
        if isinstance(val, int):
            self._value = val

    def _get_field_value(self):
        return self._value


class DateField(Field):

    def _set_field_value(self, val):
        if isinstance(val, date):
            self._value = val

    def _get_field_value(self):
        return self._value


# ------------------------------
# 3. Klasa Model z refaktoryzacją
# ------------------------------
class Model:

    def __init__(self, db_table=None):
        self.db_table = self.generate_table_for_name(self.__class__.__name__) if db_table is None else db_table

    @staticmethod
    def generate_table_for_name(name: str):
        """ Metoda zwracająca nazwę tabeli na podstawie nazwy modelu """
        return f'db_{name.lower()}'

    def get_fields(self):
        """ Pobiera wszystkie pola klasy """
        fields = {}
        for name, obj in inspect.getmembers(self):
            if isinstance(obj, Field):
                fields[name] = obj.get_fieldtype()
        return fields

    def __setattr__(self, attr, val):
        """ Obsługuje przypisywanie wartości do pól klasy """
        for name, obj in inspect.getmembers(self):
            if name == attr and isinstance(obj, Field):
                obj.value = val
                return
        super().__setattr__(attr, val)

    def __getattr__(self, attr):
        """ Zwraca wartość pola zamiast instancji Field """
        if attr in self.get_fields():
            return getattr(self.__dict__[attr], "_value", None)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

    def save(self):
        """ Generuje poprawny SQL dla zapisu modelu do bazy danych """
        fields = self.get_fields()
        values = {k: getattr(self, k) for k in fields}

        if values.get('id') is None:
            sql = f"INSERT INTO {self.db_table} ({', '.join(fields.keys())}) VALUES ({', '.join(['DEFAULT' if k == 'id' else repr(v) for k, v in values.items()])})"
        else:
            set_clause = ', '.join(f"{k} = {repr(v)}" for k, v in values.items() if k != 'id')
            sql = f"UPDATE {self.db_table} SET {set_clause} WHERE id = {values['id']}"

        return sql


# ------------------------------
# 4. Implementacja Koszyk (MutableSequence)
# ------------------------------
class Koszyk(MutableSequence):

    def __init__(self):
        self._items = []

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def __len__(self):
        return len(self._items)

    def insert(self, index, value):
        self._items.insert(index, value)

    def __repr__(self):
        return repr(self._items)


# ------------------------------
# 5. Implementacja Tydzien (Collection)
# ------------------------------
class Tydzien(Collection):

    dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

    def __contains__(self, item):
        return item in self.dni_tygodnia

    def __iter__(self):
        return iter(self.dni_tygodnia)

    def __len__(self):
        return len(self.dni_tygodnia)


# ------------------------------
# 6. Testowanie klas i metod
# ------------------------------
print("\n=== TESTOWANIE MODEL ===")
movie = Model()
print(movie.db_table)  # 'db_model'

movie = Model("custom_table")
print(movie.db_table)  # 'custom_table'

print("\n=== TESTOWANIE POL ===")
movie.title = StringField()
movie.title = "Pierwszy człowiek"
print(movie.title)  # 'Pierwszy człowiek'

movie.year = IntegerField()
movie.year = 2018
print(movie.year)  # 2018

movie.release_date = DateField()
movie.release_date = date(2018, 10, 12)
print(movie.release_date)  # '2018-10-12'

print("\n=== TESTOWANIE SQL SAVE ===")
print(movie.save())  # INSERT lub UPDATE

print("\n=== TESTOWANIE KOSZYKA ===")
koszyk = Koszyk()
koszyk.append("Jabłko")
koszyk.append("Banan")
print(koszyk)  # ['Jabłko', 'Banan']

print("\n=== TESTOWANIE TYGODNIA ===")
tydzien = Tydzien()
print("Środa" in tydzien)  # True
print(list(tydzien))  # ["Poniedziałek", ..., "Niedziela"]
