"""
#ZAD 1

import re
from collections import Counter

# Funkcja zliczająca liczbę słów, zdań i akapitów
def analiza_tekstu(tekst):
    # Zliczanie akapitów: każdy akapit to linia zakończona nową linią
    akapity = tekst.split('\n')
    liczba_akapity = len(akapity)

    # Zliczanie zdań: każde zdanie kończy się kropką, pytajnikiem lub wykrzyknikiem
    zdania = re.split(r'[.!?]', tekst)
    liczba_zdan = len([zdanie for zdanie in zdania if len(zdanie.strip()) > 0])

    # Zliczanie słów: każde słowo to ciąg znaków alfanumerycznych
    slowa = re.findall(r'\b\w+\b', tekst)
    liczba_slow = len(slowa)

    return liczba_slow, liczba_zdan, liczba_akapity

# Funkcja filtrująca najczęściej występujące słowo, z wykluczeniem "stop words"
def najczesciej_wystepujace_slowo(tekst, stop_words):
    # Znajdowanie wszystkich słów w tekście
    slowa = re.findall(r'\b\w+\b', tekst.lower())  # Normalizacja do małych liter
    # Filtrujemy słowa, usuwając stop words
    slowa_filtr = filter(lambda x: x not in stop_words, slowa)
    # Zliczanie częstości występowania słów
    counter = Counter(slowa_filtr)
    # Zwracamy najczęściej występujące słowo
    return counter.most_common(1)  # Zwracamy tylko jedno najczęstsze słowo

# Funkcja do transformacji słów zaczynających się na 'a' lub 'A' na ich odwrotność
def transformacja_tekst(tekst):
    # Dzielimy tekst na słowa
    slowa = re.findall(r'\b\w+\b', tekst)
    # Zastosowanie transformacji tylko do słów zaczynających się na 'a' lub 'A'
    transformed_words = map(lambda word: word[::-1] if word.lower().startswith('a') else word, slowa)
    # Łączenie słów z powrotem w tekst
    return ' '.join(transformed_words)

# Przykład użycia

tekst = '''
Apple is a fruit. It is often used in pies. Amazing fruit, isn't it? Apples are delicious and healthy.
Another important thing is that apples come in different colors. A big apple is a good source of vitamins.
'''

# Stop words do wykluczenia
stop_words = {"i", "a", "the", "is", "in", "on", "and", "to", "of", "it", "this", "that"}

# 1. Analiza tekstu
liczba_slow, liczba_zdan, liczba_akapity = analiza_tekstu(tekst)
print(f"Liczba słów: {liczba_slow}")
print(f"Liczba zdań: {liczba_zdan}")
print(f"Liczba akapitów: {liczba_akapity}")

# 2. Najczęściej występujące słowo
najczestsze = najczesciej_wystepujace_slowo(tekst, stop_words)
if najczestsze:
    slowo, liczba = najczestsze[0]
    print("\nNajczęściej występujące słowo (po wykluczeniu stop words):")
    print(f"{slowo}: {liczba}")
else:
    print("\nBrak słów po wykluczeniu stop words.")

# 3. Transformacja słów zaczynających się na 'a' lub 'A'
tekst_transformed = transformacja_tekst(tekst)
print("\nTekst po transformacji (odwrócone słowa zaczynające się na 'a' lub 'A'):")
print(tekst_transformed)


"""

"""
#ZAD 2

import numpy as np


# Funkcje walidacyjne
def validate_addition(matrix1, matrix2):
    '''Walidacja dla dodawania macierzy: muszą mieć te same wymiary'''
    return matrix1.shape == matrix2.shape


def validate_multiplication(matrix1, matrix2):
    '''Walidacja dla mnożenia macierzy: liczba kolumn w pierwszej musi być równa liczbie wierszy w drugiej'''
    return matrix1.shape[1] == matrix2.shape[0]


def validate_transposition(matrix):
    '''Walidacja dla transponowania: nie ma żadnych szczególnych warunków'''
    return True


# Funkcja wykonująca operację na macierzach
def execute_operation(operation, matrix1, matrix2=None):
    '''Funkcja wykonująca operację na macierzach na podstawie stringa.'''

    # Operacje dodawania
    if operation == 'add':
        if validate_addition(matrix1, matrix2):
            return matrix1 + matrix2
        else:
            return "Błąd: macierze muszą mieć te same wymiary do dodawania."

    # Operacje mnożenia
    elif operation == 'multiply':
        if validate_multiplication(matrix1, matrix2):
            return matrix1.dot(matrix2)
        else:
            return "Błąd: liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy."

    # Operacje transponowania
    elif operation == 'transpose':
        if validate_transposition(matrix1):
            return matrix1.T
        else:
            return "Błąd: nie można transponować tej macierzy."

    else:
        return "Błąd: nieznana operacja."


# Funkcja do wykonywania operacji na macierzach dynamicznie (z użyciem eval)
def process_operation(string_operation, matrix1, matrix2=None):
    '''Funkcja przyjmuje string operacji i wykonuje ją.'''

    # Definiowanie możliwych operacji
    operations = {
        'add': 'add',
        'multiply': 'multiply',
        'transpose': 'transpose'
    }

    # Przetwarzanie operacji przy użyciu eval
    try:
        # Jeśli mamy dwie macierze (np. dodawanie lub mnożenie)
        if matrix2 is not None:
            return execute_operation(operations[string_operation], matrix1, matrix2)
        # Jeśli mamy jedną macierz (np. transponowanie)
        else:
            return execute_operation(operations[string_operation], matrix1)
    except KeyError:
        return "Błąd: nieznana operacja."
    except Exception as e:
        return f"Błąd: {str(e)}"


# Przykład użycia

# Tworzenie przykładowych macierzy
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8, 9], [10, 11, 12]])
matrix_c = np.array([[13, 14, 15], [16, 17, 18],[19, 20, 21]])

# Testowanie operacji
operation_1 = "add"  # Dodawanie
operation_2 = "multiply"  # Mnożenie
operation_3 = "transpose"  # Transponowanie

# Wywołanie funkcji z operacjami
print("Wynik dodawania macierzy a i b:")
print(process_operation(operation_1, matrix_a, matrix_b))  # Dodawanie

print("\nWynik mnożenia macierzy a i b:")
print(process_operation(operation_2, matrix_a, matrix_b))  # Mnożenie błąd
print("\nWynik mnożenia macierzy a i c:")
print(process_operation(operation_2, matrix_a, matrix_c))  # Mnożenie poprawne

print("\nWynik transponowania macierzy a:")
print(process_operation(operation_3, matrix_a))  # Transponowanie

"""

"""
#ZAD 3

def analyze_data(data):
    # Filtrujemy liczby (int i float)
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))

    # Filtrujemy napisy (stringi)
    strings = list(filter(lambda x: isinstance(x, str), data))

    # Filtrujemy krotki (tuple)
    tuples = list(filter(lambda x: isinstance(x, tuple), data))

    # Znajdowanie największej liczby
    largest_number = max(numbers, default=None)  # Domyślnie None jeśli brak liczb

    # Znajdowanie najdłuższego napisu
    longest_string = max(strings, key=len, default=None)  # Domyślnie None jeśli brak napisów

    # Znajdowanie krotki o największej liczbie elementów
    largest_tuple = max(tuples, key=len, default=None)  # Domyślnie None jeśli brak krotek

    # Zwracamy wyniki
    return largest_number, longest_string, largest_tuple


# Przykład użycia
data = [42, "Hello", (1, 2, 3), 3.14, "World", (1, 2), "Python", (5, 6, 7, 8)]

largest_number, longest_string, largest_tuple = analyze_data(data)

print(f"Największa liczba: {largest_number}")
print(f"Najdłuższy napis: {longest_string}")
print(f"Krotka o największej liczbie elementów: {largest_tuple}")

"""

#ZAD 4

import numpy as np
from functools import reduce


# Funkcja przyjmująca operację (string) oraz listę macierzy
def matrix_operations(operacja, matrices):
    '''
    Funkcja wykonuje operację na liście macierzy, używając reduce.

    operacja: String (np. 'sum', 'multiply') - operacja na macierzach
    matrices: lista macierzy np. [matrix1, matrix2, matrix3] - lista macierzy do przetworzenia

    Zwraca wynik po zastosowaniu operacji na wszystkich macierzach.
    '''

    # Definiowanie operacji
    operations = {
        'sum': lambda x, y: np.add(x, y),  # Dodawanie
        'multiply': lambda x, y: np.dot(x, y),  # Mnożenie
    }

    # Sprawdzanie, czy operacja jest zdefiniowana
    if operacja not in operations:
        return f"Błąd: Nieznana operacja '{operacja}'."

    # Użycie reduce() do zastosowania operacji na wszystkich macierzach
    return reduce(operations[operacja], matrices)


# Funkcja umożliwiająca użytkownikowi dodanie niestandardowej operacji
def define_custom_operation():
    '''
    Funkcja umożliwia użytkownikowi zdefiniowanie niestandardowej operacji
    w formie stringa. Wynikowa operacja jest przekazywana do eval() w celu jej
    zastosowania w matrix_operations.
    '''
    # Prosimy użytkownika o wpisanie operacji
    print("Wprowadź operację jako wyrażenie Pythona (np. 'x + y' dla dodawania, 'x @ y' dla mnożenia):")
    operation_str = input()

    # Definicja niestandardowej operacji
    def custom_operation(x, y):
        return eval(operation_str)

    return custom_operation


# Przykład użycia

# Tworzymy przykładowe macierze
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix3 = np.array([[9, 10], [11, 12]])

# Lista macierzy
matrices = [matrix1, matrix2, matrix3]

# Wybór operacji - np. suma
operation = 'sum'

# Wywołanie funkcji z operacją 'sum' i listą macierzy
result = matrix_operations(operation, matrices)

print("Wynik operacji 'sum':")
print(result)

# Wybór niestandardowej operacji
custom_op = define_custom_operation()

# Zastosowanie niestandardowej operacji do połączenia macierzy
result_custom = reduce(custom_op, matrices)

print("Wynik niestandardowej operacji:")
print(result_custom)


