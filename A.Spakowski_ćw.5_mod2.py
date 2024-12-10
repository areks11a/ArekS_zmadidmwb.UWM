print("\nĆwiczenie 5 - osobny plik")

# 5. Przejdź na stronę https://pyformat.info/, a następnie zapisz w oddzielnym pliku .py i wykonaj 5
# wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach
# z tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby, znakiem,
# wypełnieniem spacji itp.). Przerób zaprezentowane tam przykłady na postać z użyciem f-string.

print('\n1_Dodanie "_" do 10 pozycji\nnew.format:')
print('{:_<10}'.format('test'))

print('f-string:')
print(f'{"test":_<10}')


print('\n2_Wyśrodkowanie w 10 pozycjach\nnew.format:')
print('{:^10}'.format('test'))
print('f-string:')
print(f'{"test":^10}')

print('\n3_Uzupełnienie pól:')
print('new.format:')
arg1='one'
arg2=2
print('{} {}'.format('one', 2 ))
print('f-string')
print(f'{arg1} {arg2}')

print('\n4_Uzupełnienie pól "na skos":')
print('new.format:')
print('{1} {0}'.format('one', 2 ))
print('f-string:')
print(f'{arg2} {arg1}')



print('\n5_Skracanie długiego zapisu:')
print('new.format:')
print('{:.5}'.format('xylophone'))
print('f-string:')
dlugieSlowo='xylophone'
print(f'{dlugieSlowo:.5}')
