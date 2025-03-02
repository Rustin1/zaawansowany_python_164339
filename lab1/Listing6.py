class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Field({self.value})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.value == other.value
        else:
            return False


class KoloFortuny:

    def __init__(self, *fields):
        self.fields = [tuple[int, Field]]
        if fields:
            self.fields = list(zip(range(1, len(fields) + 1), [Field(val) for val in fields]))

    def __str__(self):
        return f"KoloFortuny({self.fields})"

    def __getitem__(self, idx):
        return self.fields[idx][1]

    def __setitem__(self, idx, val: Field):
        if isinstance(val, Field):
            self.fields[idx] = (idx + 1, val)
        else:
            raise TypeError("Można wstawić tylko wartość typu Field!")

    def __iter__(self):
        return iter(self.fields)

    def __contains__(self, other):
        if isinstance(other, Field):
            return other in [val for _, val in self.fields]
        else:
            raise TypeError("Nie umiem znaleźć innych elementów niż te typu Field!")


if __name__ == '__main__':

    kolo = KoloFortuny(100, 'Bankrut', 50, 300, 'Niespodzianka', 1000)
    print(kolo)
    print(kolo[3])
    kolo[3] = Field(750)
    # odkomentuj poniższą linię i sprawdź działanie
    # kolo[3] = 750

    for field in kolo:
        print(field)

    print(Field(750) in kolo)

    kolo()