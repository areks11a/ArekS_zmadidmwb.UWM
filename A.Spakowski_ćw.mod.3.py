# Zadanie 1
# Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej
# liście a pozostałe 5 znalazło się w nowej liście.
print('1_Zadanie1:')
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista,'liczba wartości w liście:', len(lista))

srodek=len(lista)//2

nowaLista1 = lista[:srodek]
nowaLista2 = lista[srodek:]

print(nowaLista1)
print(nowaLista2)


# Zadanie 2
# Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę
# posortowaną malejąco.

print('\n2_Zadanie 2:')
polLista=nowaLista1+nowaLista2
print(polLista)

nowaLista1.extend(nowaLista2)
print(nowaLista1)

polLista.insert(0,0) #dodje 0 na wskazanej pozycji
# polLista.extend('0') - dodaje 0 na koncu

print(polLista)

posortowana=polLista.sort(reverse=True)
print(polLista)


# Zadanie 3
# Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funkcję input(). Następnie
# wyświetl ciąg unikalnych znaków z wczytanego zdania, zapisanych alfabetycznie małymi literami.*
# * wykorzystaj rzutowanie typu str na set oraz set na list i użyj funkcji sortującej listę

print('\n3_Zadanie3:')

zdanie=input('Wpisz dowolny tekst:')
# zdanie='Ala ma 123'

maleZdanie=zdanie.lower()
print(maleZdanie)

zbiórZnaków=set(maleZdanie)
print(zbiórZnaków)

listaZnakow=list(zbiórZnaków)
print(listaZnakow)

posortowaneZnaki=listaZnakow.sort()
print(listaZnakow)

# Zadanie 4
# Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1) a wartościami nazwy polskich
# miesięcy.

print('\n4_Zadanie4:')

miesiacePL={
     1:"styczeń",
     2:"luty",
     3:"marzec",
     4:"kwiecień",
     5:"maj",
     6:"czerwiec",
     7:"lipiec",
     8:"sierpień",
     9:"wrzesień",
     10:"październik",
     11:"listopad",
     12:"grudzień" }

print(miesiacePL)


# Zadanie 5
# Stwórz podobny słownik jak w zadaniu 4, ale z angielskimi nazwami miesięcy. Połącz teraz słowniki tak, żeby
# przykładowo dla kwietnia, dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez
# months['en'][4].
print("\n5_Zadanie5:")
miesiaceEN={
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"}

print(miesiaceEN)

miesiacePLEN={"pl":miesiacePL,"en":miesiaceEN}
print(miesiacePLEN)

print(miesiacePLEN['en'][4])
print(miesiacePLEN['pl'][4])



# Zadanie 6
# Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, który będzie
# zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie miał przypisaną wartość 1.
# Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1}
print("\n6_Zadanie6:")

bazaDlaKluczy='Marianna'
listaUnikZnak=set(bazaDlaKluczy)
keys = listaUnikZnak
value = 1
new_dict = dict.fromkeys(keys, value)
print(new_dict)


# Zadanie 7
print('\n7_Zadanie7:')

# Wykorzystaj moduł string (dodaje się go poprzez instrukcję import string zapisaną zazwyczaj na początku
# skryptu) i następnie:
import string

# wczytaj ze standardowego wejścia dowolny łańcuch znaków,
lancuch7=input('Wpisz dowolny łańcuch znaków:')
# lancuch7='QWqw12'

# używając formatowania znaków wyświetl ile znaków oraz jaki procent (zamienionych na małe litery) z
# nich pokrywa się ze zbiorem znaków z: string.ascii_lowercase, string.digits (podpowiedź:
# operator in)
lancuch7L=lancuch7.lower()
print('male znaki:',lancuch7L)

# liczba_pasujących=sum(1 for znak in lancuch7L if znak in string.ascii_lowercase)
# print(liczba_pasujących)

asciiZb=set(string.ascii_lowercase)
digitsZb=set(string.digits)

lancuch7Lzb=set(lancuch7L)
print('zbiór unikalnych:',lancuch7Lzb)

liczbaAscii=(lancuch7Lzb & asciiZb)
liczbaDigit=(lancuch7Lzb & digitsZb)

print('\nwspólne z ascii:',liczbaAscii)
print('wspólne z digit:',liczbaDigit)

procentAscii=f'{len(liczbaAscii)/len(lancuch7L)*100:.2f}'
procentDigit=f'{len(liczbaDigit)/len(lancuch7L)*100:.2f}'

print('\nliczba wspólnych z ascii:',len(liczbaAscii))
print('liczba wspólnych z digit:',len(liczbaDigit))

print('\nliczba znaków we wprowadzonym zbiorze:',len(lancuch7L))
print('\nunikaty w ascii vs wszystkie znaki w zbiorze:',procentAscii,'%')
print('unikaty w digit vs wszystkie znaki w zbiorze:',procentDigit,'%')

print('\nW zbiorze  "',lancuch7L,'"  występuje',len(liczbaAscii),'unikalnych znaków wspólnych ze zbiorem string.ascii_lowercase, \nco stanowi',procentAscii,'% tego zbioru.')
print('\nW zbiorze  "',lancuch7L,'"  występuje',len(liczbaDigit),'unikalnych znaków wspólnych ze zbiorem string.digit, \nco stanowi',procentDigit,'% tego zbioru.')


# Przykład:
# Wejście (input):
# Ala ma kota.
# Wyjście (output):
# W zdaniu 'Ala ma kota.' występuje 6 znaków wspólnych ze zbiorem
# string.ascii_lowercase, co stanowi 23.00 % tego zbioru.
# W zdaniu 'Ala ma kota.' występuje 0 znaków wspólnych ze zbiorem string.digits, co
# stanowi 0.00 % tego zbioru.

# Zadanie 8
print('\n8_Zadanie8:')

# Napisz kod, w którym pobierzesz za pomocą funkcji input() 3 wartości przypisując je do zmiennych: start,
# stop oraz step. Następnie użyj ich jako parametrów funkcji range i wykorzystując przykłady z listingu 10
# wypisz wszystkie wartości ciągu wygenerowane przez tę funkcję. Zwróć uwagę na typ danych, który zwraca
# funkcja input() - będzie konieczna konwersja (rzutowanie).
iNstart=input('Wpisz wartość początku ciągu (liczba):')
iNstop=input('Wpisz wartość końca ciągu (liczba):')
iNstep=input('Wpisz wartość konstruktora ciągu (liczba):')

start=int(iNstart)
stop=int(iNstop)
step=int(iNstep)

for i in range(start,stop,step):
    print( i )

# lista z elementów funkcji range
lista = list(range(start,stop,step))
print('Ciąg w formie listy:',lista)

