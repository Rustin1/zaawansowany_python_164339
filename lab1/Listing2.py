class whoops: pass

wh = whoops()

# a to?
class whoopsi: ...


# podobny do powyższego zapis znajdziemy w plikach z rozszerzeniem .pyi, które są plikami zawierającymi
# tylko szkielet (ang. stub), który może zawierać tylko sygnatury funkcji, klas i ich metod
# które pełnią funkcję interfejsów w Pythonie, których nie możemy implementować w sposób znany chociażby
# z języka Java czy C#. Można to np. zobaczyć w pliku builtins.pyi, ale i wielu innych


wh2 = whoopsi()
print(wh.__class__, wh2.__class__)