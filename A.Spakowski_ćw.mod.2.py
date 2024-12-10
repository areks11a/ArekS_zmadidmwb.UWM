# Ćwiczenia
print('Ćwiczenie 1')
# 1. Napisz fragment kodu, który wczyta trzy zmienne ze standardowego wejścia (np. funkcja input()):
# linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
# separator źródłowy
# separator docelowy
zmienne = input ('Wpisz dowolne wyrażenia rozdzielone dowolnym (tym samym) znakiem:\n')
sepZrodlowy = input('Wpisz jakiego separatora użyłeś:\n')
sepDocelowy = input('Wpisz na jaki separator chcesz go zamienić:\n')

# Następnie zaimplementuj z użyciem metod str.split() oraz str.join() podzielenie danych wejściowych
# pierwszym separatorem,
words = zmienne.split(sepZrodlowy)
print(words)

# połączenie i wypisanie danych połączonych drugim separatorem.
newString = sepDocelowy.join(words)
print('pierwsza metoda:',newString)
#
# Czy można to
# zrobić prościej wykorzystując inne wbudowane metody?
newStr2 = zmienne.replace(sepZrodlowy,sepDocelowy)
print('druga metoda:',newStr2)

# 2. Użyj funkcji input() aby pobrać łańcuch znaków z klawiatury
print('\nĆwiczenie 2')
łańcuch = input('Wpisz dowolny łańcuch znaków:')

#
# i z użyciem wycinków (slice) wykonaj:
# podziel łańcuch na dwie części, w miarę możliwości równe, ale jeżeli długość łańcucha jest nieparzysta,
# np. 11 znaków to pierwszy ma długość 5, a drugi 6.
liczbaZnaków = len(łańcuch)
print('Liczba znaków w łańcuchu:',liczbaZnaków)

połowaZdzielBEZresz = liczbaZnaków//2
print('Pierwsza część łańcucha - długość:',połowaZdzielBEZresz)

drugaPołowa = liczbaZnaków - połowaZdzielBEZresz
print('Druga część łańcucha - długość:',drugaPołowa)

pierwszyŁańcuch=łańcuch[:połowaZdzielBEZresz]
drugiŁańcuch=łańcuch[połowaZdzielBEZresz:]
#
# Wyświetl te łańcuchy w oknie konsoli.
print('Łańcuch1:',pierwszyŁańcuch)
print('Łańcuch2:',drugiŁańcuch)

# wyświetl łańcuch składający się z co drugiego znaku licząc od końca łańcucha
print('Co drugi znak od końca:',łańcuch[::-2])

# 3. Wyświetl na konsoli dowolny ciąg znaków i wykorzystaj wbudowane metody:
print('\nĆwiczenie 3')
łańcuch2=input('wpisz cokolwiek:')
# title(),
print(łańcuch2.title())

# capitalize(),
print(łańcuch2.capitalize())

# zfill(),
print(łańcuch2.zfill(10))

# upper(),
print(łańcuch2.upper())

# count(),
print(łańcuch2.count('a'))

# center().
print(łańcuch2.center(10))

# 4. Wprowadź z klawiatury dowolny łańcuch znaków i zapisz go do zmiennej.
print('\nĆwiczenie 4')
wejscie = input('Wpisz dowolne znaki:')
#
# Następnie bazując na przykładzie poniżej zapisz również wyniki dla metod
print(f"PRZYKŁAD: Łańcuch {wejscie} isdecimal:{wejscie.isdecimal()}")
#
# isalpha(),
# isascii(),
# isprintable(),
# istitle(),
# isupper()
print(f'Łańcuch {wejscie} isalpha: {wejscie.isalpha()}')
print(f'Łańcuch {wejscie} isascii: {wejscie.isascii()}')
print(f'Łańcuch {wejscie} isprintable: {wejscie.isprintable()}')
print(f'Łańcuch {wejscie} isupper: {wejscie.isupper()}')


print("\nĆwiczenie 5 - osobny plik")
input('Wciśnij ENTER żeby przejść dalej')
# 5. Przejdź na stronę https://pyformat.info/, a następnie zapisz w oddzielnym pliku .py i wykonaj 5
# wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach
# z tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby, znakiem,
# wypełnieniem spacji itp.). Przerób zaprezentowane tam przykłady na postać z użyciem f-string.

print('\nĆwiczenie 6')
input('Wciśnij ENTER żeby uruchomić')
# 6. Wykorzystując listing 7 wypisz na konsoli 10 wybranych znaków niestandardowych (np. litery z alfabetu
# greckiego, symbole walut - (funt, bitcoin)) wypisując jednocześnie jego kod z tablicy unicode.

print('Symbol:','\u03a3','--> UNICODE: 03A3')
print('\u00a7','--> 00A7')
print('\u03a9','--> 03A9')
print('\u00a5','--> 00A5')
print('\u00ae','--> 00AE')
print('\u00a3','--> 00A3')
print('\u20bf','--> 20BF')
print('\u2197','--> 2197')
print('\u221b','--> 221B')
print('\u2328','--> 2328')
