import random
import csv

# Funkcjonalność, którą ma dostarczać moduł:
#  Wczytanie datasetu

def pobierz_sciezke():
    print("WCZYTANIE DATASETU")
    sciezka = input("Podaj ścieżkę do pliku CSV (domyślnie 'iris.csv'): ") or "iris.csv"
    return sciezka

def czy_ma_naglowki():
    odp = input("Czy plik zawiera nagłówki? (tak/nie, domyślnie: tak): ")
    return odp in ["tak", ""]

def wczytaj_dane(sciezka, naglowki=True):
    try:
        with open(sciezka, encoding='utf-8') as irysy:
            reader = csv.reader(irysy)
            dane = list(reader)
        if naglowki:
            naglowki_kolumn = dane[0]
            dane = dane[1:]
        else:
            naglowki_kolumn = None
        return naglowki_kolumn, dane
    except FileNotFoundError:
        print(f"Nie znaleziono pliku. Używam domyślnego pliku 'iris.csv'.")

# Funkcjonalność, którą ma dostarczać moduł:
#  Wypisanie etykiet

def wypisz_etykiety(naglowki_kolumn):
    print("\nWYPISANIE ETYKIET")
    if naglowki_kolumn:
        print(naglowki_kolumn)
    else:
        print("Brak nagłówków w tym pliku.")

# Funkcjonalność, którą ma dostarczać moduł:
#  Wypisanie danych datasetu

def wypisz_dane(dane):
    print("\nWYPISANIE DANYCH DATASETU")
    try:
        start = int(input("Podaj numer początkowego wiersza: "))
        koniec = int(input("Podaj numer końcowego wiersza: "))

        if start < 0 or koniec > len(dane) or start >= koniec:
            raise ValueError
    except ValueError:
        print("Nieprawidłowy zakres. Wyświetlam wszystkie wiersze.")
        start, koniec = 0, len(dane)

    for wiersz in dane[start:koniec]:
        print(", ".join(wiersz))

# Funkcjonalność, którą ma dostarczać moduł:
#  Podział datasetu na zbiór treningowy, testowy i walidacyjny

def podziel_dataset(dane):
    print("\nPODZIAŁ DATASETU NA ZBIORY")
    while True:
        try:
            train_pct = float(input("    Podaj procentowy rozmiar zbioru treningowego (np. 70): ")) / 100
            test_pct = float(input("    Podaj procentowy rozmiar zbioru testowego (np. 15): ")) / 100
            val_pct = 1.0 - (train_pct + test_pct)

            if train_pct <= 0 or test_pct <= 0 or val_pct < 0:
                raise ValueError
            break
        except ValueError:
            print("    Błędne wartości")

    random.shuffle(dane)
    n = len(dane)
    train_end = int(train_pct * n)
    test_end = train_end + int(test_pct * n)

    train = dane[:train_end]
    test = dane[train_end:test_end]
    val = dane[test_end:]

    print("Parametry utworzonych zbiorów:")
    print(f"    Zbiór treningowy: {len(train)} rekordów ({train_pct * 100:.1f}%)")
    print(f"    Zbiór testowy: {len(test)} rekordów ({test_pct * 100:.1f}%)")
    print(f"    Zbiór walidacyjny: {len(val)} rekordów ({val_pct * 100:.1f}%)\n")

    return train, test, val

# Funkcjonalność, którą ma dostarczać moduł:
#  Wypisz liczbę i liczebność klas decyzyjnych

def liczba_klas(dane):
    klasy = {}
    for wiersz in dane:
        klasa = wiersz[-1]
        klasy[klasa] = klasy.get(klasa, 0) + 1
    return klasy

def filtruj_klase(dane, klasa):
    return [wiersz for wiersz in dane if wiersz[-1] == klasa]

# Funkcjonalność, którą ma dostarczać moduł:
#  Wypisz dane dla podanej wartości klasy decyzyjnej

def wypisz_dane_klasy(dane):
    print("\nWYPISANIE DANYCH DLA PODANEJ KLASY DECYZYJNEJ")
    klasy = liczba_klas(dane)
    klasa = input("Podaj nazwę klasy decyzyjnej do wyświetlenia jej wierszy: ").strip()
    dane_klasy = filtruj_klase(dane, klasa)
    if dane_klasy:
        print(f"Wiersze dla klasy '{klasa}':")
        for wiersz in dane_klasy:
            print(", ".join(wiersz))
    else:
        print(f"Brak danych dla klasy '{klasa}'.")

# Funkcjonalność, którą ma dostarczać moduł:
#  Zapisanie danych do pliku csv

def zapisz_do_csv(dane, naglowki, nazwa_pliku):
    with open(nazwa_pliku, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if naglowki:
            writer.writerow(naglowki)
        writer.writerows(dane)
    print(f"Dane zapisano do '{nazwa_pliku}'")

# TESTOWANIE MODUŁU
if __name__ == "__main__":

    sciezka = pobierz_sciezke()
    naglowki = czy_ma_naglowki()
    etykiety, dataset = wczytaj_dane(sciezka, naglowki)

    if dataset:
        wypisz_etykiety(etykiety)
        wypisz_dane(dataset)

        train, test, val = podziel_dataset(dataset)

        klasy_dec = liczba_klas(dataset)
        print("LICZBA I LICZEBNOŚĆ KLAS DECYZYJNYCH\n", klasy_dec)
        wypisz_dane_klasy(dataset)

        print("\nZAPISANIE DANYCH DO PLIKÓW CSV")
        nazwa_train = input("Podaj nazwę pliku dla zbioru treningowego (domyślnie 'tren.csv'): ") or "tren.csv"
        nazwa_test = input("Podaj nazwę pliku dla zbioru testowego (domyślnie 'test.csv'): ") or "test.csv"
        nazwa_val = input("Podaj nazwę pliku dla zbioru walidacyjnego (domyślnie 'walid.csv'): ") or "walid.csv"

        zapisz_do_csv(train, etykiety, nazwa_train)
        zapisz_do_csv(test, etykiety, nazwa_test)
        zapisz_do_csv(val, etykiety, nazwa_val)
