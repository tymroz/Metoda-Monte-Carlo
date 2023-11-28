import random
import numpy as np
import matplotlib.pyplot as plt

# Definicje funkcji, obliczającej odleglosc punktu(x,y) od punktu(0,0)
def func1(x, y):
    r = x**2 + y**2
    return r

# Liczba powtórzeń i generowanie wartości n od 50 d0 5000
k = 50
n_values = range(50, 5001, 50)

l = len(n_values)

# Przechowywanie wyników
results = []

# Generowanie punktów (x,y) i sumowanie, ile z wygenerowanych punktów 'wpadło do koła'
for n in n_values:
    approximations = []
    all_points = []

    for _ in range(k):
        points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for t in range(n)]
        C = sum(1 for x, y in points if func1(x, y)<=1)
        approximations.append(4 * C / n)
        all_points.extend(points)

    results.append(approximations)

# Obliczanie średnich wyników
avg_results = np.mean(results, axis=1)

# Wypisywanie otrzymanej średniej wartości pi dla n=5000
print("średni wynik alorytmu dla n=5000: " + str(avg_results[l-1]))

# Rysowanie wykresu
plt.figure("wartosc liczby π", figsize=(10, 6))
plt.subplot(111)
plt.title("szacowana wartosc π")
for i in range(l):
    plt.scatter([n_values[i]] * k, results[i], color='blue', marker='o', alpha=0.3)  # Punkty z każdego powtórzenia
    plt.scatter(n_values[i], avg_results[i], color='red', marker='o')  # Średnia wyników dla danego n
plt.axhline(np.pi, color='green') # Dokładna wartość pi
plt.show()