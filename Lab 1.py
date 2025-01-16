"""
#ZAD 1

def podzial_paczek(paczki, max_waga):
    paczki.sort(reverse=True)  # Sortowanie paczek w porządku malejącym
    kursy = []  # Lista, która będzie przechowywać kursy

    # Iterowanie przez paczki
    for paczka in paczki:
        # Szukamy kursu, do którego możemy dodać paczkę
        dodana = False
        for kurs in kursy:
            if sum(kurs) + paczka <= max_waga:
                kurs.append(paczka)
                dodana = True
                break

        # Jeśli paczka nie została dodana do żadnego kursu, tworzymy nowy kurs
        if not dodana:
            kursy.append([paczka])

    return len(kursy), kursy


# Przykład użycia
paczki = [2, 5, 4, 7, 3, 1, 8]
max_waga = 10
liczba_kursow, kursy = podzial_paczek(paczki, max_waga)

print(f"Liczba kursów: {liczba_kursow}")
print("Paczki w każdym kursie:")
for i, kurs in enumerate(kursy, 1):
    print(f"Kurs {i}: {kurs}")

"""

"""
#ZAD 2

from collections import deque

# Funkcja BFS
def bfs(graph, start, end):
    # Zainicjowanie kolejki (deque) i zbioru odwiedzonych wierzchołków
    queue = deque([(start, [start])])  # (wierzchołek, ścieżka)
    visited = set([start])

    # Funkcja rekurencyjna BFS
    def bfs_rec(queue, visited):
        if not queue:
            return []  # Jeśli kolejka jest pusta, nie znaleziono ścieżki

        # Pobierz pierwszy wierzchołek i jego ścieżkę
        current_node, path = queue.popleft()

        # Sprawdź, czy osiągnęliśmy cel
        if current_node == end:
            return path

        # Przejdź po sąsiadach wierzchołka
        neighbors = graph.get(current_node, [])
        new_neighbors = filter(lambda x: x not in visited, neighbors)
        new_paths = map(lambda neighbor: (neighbor, path + [neighbor]), new_neighbors)

        # Dodaj nowych sąsiadów do kolejki i zaktualizuj zbiór odwiedzonych wierzchołków
        new_queue = list(queue) + list(new_paths)
        new_visited = visited | set(neighbors)

        return bfs_rec(deque(new_queue), new_visited)

    # Wywołanie rekurencyjnej funkcji BFS
    return bfs_rec(queue, visited)


# Przykład grafu jako słownik
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Testowanie funkcji BFS
start = 'A'
end = 'F'
shortest_path = bfs(graph, start, end)

print(f"Najkrótsza ścieżka od {start} do {end}: {shortest_path}")

"""

"""

#ZAD 3

from functools import reduce


def optymalizuj_zadania_funkcyjnie(zadania):
    # Sortowanie zadania po czasie wykonania rosnąco, a potem po nagrodzie malejąco
    posortowane_zadania = sorted(zadania, key=lambda x: (x[0], -x[1]))

    # Funkcja obliczająca całkowity czas oczekiwania i zysk
    def oblicz_wyniki(acc, zadanie):
        czas_oczekiwania, calkowity_czas, calkowity_zysk = acc
        czas, nagroda = zadanie
        czas_oczekiwania += czas
        calkowity_czas += czas_oczekiwania
        calkowity_zysk += nagroda
        return (czas_oczekiwania, calkowity_czas, calkowity_zysk)

    # Reduce używane do obliczeń
    wynik = reduce(oblicz_wyniki, posortowane_zadania, (0, 0, 0))

    return posortowane_zadania, wynik[1], wynik[2]


# Przykład
zadania = [(4, 50), (2, 30), (3, 40), (1, 20)]
kolejnosc, calkowity_czas, calkowity_zysk = optymalizuj_zadania_funkcyjnie(zadania)

print("Optymalna kolejność zadań:", kolejnosc)
print("Całkowity czas oczekiwania:", calkowity_czas)
print("Całkowity zysk:", calkowity_zysk)


"""

#ZAD 4

# Implementacja Proceduralna (Dynamiczne Programowanie)
def plecak_proceduralnie(wagi, wartosci, pojemnosc):
    n = len(wagi)

    # Tworzymy tablicę dp o wymiarach (n+1) x (pojemnosc+1)
    dp = [[0] * (pojemnosc + 1) for _ in range(n + 1)]

    # Wypełniamy tablicę dp
    for i in range(1, n + 1):
        for j in range(1, pojemnosc + 1):
            if wagi[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wagi[i - 1]] + wartosci[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    # Odtwarzanie przedmiotów, które zostały wybrane do plecaka
    przedmioty = []
    j = pojemnosc
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            przedmioty.append(i - 1)  # Dodajemy indeks przedmiotu (i-1)
            j -= wagi[i - 1]

    przedmioty.reverse()  # Aby przedmioty były w kolejności
    return dp[n][pojemnosc], przedmioty


# Implementacja Funkcyjna (Rekurencyjne podejście)
def plecak_funkcyjnie(wagi, wartosci, pojemnosc, n):
    if n == 0 or pojemnosc == 0:
        return 0, []

    # Jeśli przedmiot nie zmieści się w plecaku
    if wagi[n - 1] > pojemnosc:
        return plecak_funkcyjnie(wagi, wartosci, pojemnosc, n - 1)

    # Jeśli można dodać przedmiot
    z_w = plecak_funkcyjnie(wagi, wartosci, pojemnosc - wagi[n - 1], n - 1)
    bez_w = plecak_funkcyjnie(wagi, wartosci, pojemnosc, n - 1)

    # Wybieramy lepszą opcję (z przedmiotem lub bez)
    if z_w[0] + wartosci[n - 1] > bez_w[0]:
        przedmioty = z_w[1] + [n - 1]
        return z_w[0] + wartosci[n - 1], przedmioty
    else:
        return bez_w


# Przykładowe dane wejściowe
wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 7]
pojemnosc = 7

# Wywołanie podejścia proceduralnego
maks_wartosc_proceduralnie, przedmioty_proceduralnie = plecak_proceduralnie(wagi, wartosci, pojemnosc)
print("Proceduralne podejście:")
print(f"Maksymalna wartość: {maks_wartosc_proceduralnie}")
print(f"Przedmioty do plecaka: {przedmioty_proceduralnie}")

# Wywołanie podejścia funkcyjnego
maks_wartosc_funkcyjnie, przedmioty_funkcyjnie = plecak_funkcyjnie(wagi, wartosci, pojemnosc, len(wagi))
print("\nFunkcyjne podejście:")
print(f"Maksymalna wartość: {maks_wartosc_funkcyjnie}")
print(f"Przedmioty do plecaka: {przedmioty_funkcyjnie}")



