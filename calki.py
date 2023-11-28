import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definicje funkcji
def func1(x):
    y = np.cbrt(x)
    return y

def func2(x):
    y = np.sin(x)
    return y

def func3(x):
    y = 4*x*(1-x)**3
    return y

# Przedziały
a1, b1 = 0, 8
a2, b2 = 0, np.pi
a3, b3 = 0, 1

# Maksimum funkcji na odpowiednich przedziałach
M1 = func1(b1)
M2 = 1
M3 = func3(1/4)

# Liczba powtórzeń i wartości n
k = 50
n_values = range(50, 5001, 50)

# Oblicz dokładne wartości całek
exact_integral1, t = quad(func1, a1, b1)
exact_integral2, t = quad(func2, a2, b2)
exact_integral3, t = quad(func3, a3, b3)

# Przechowywanie wyników
results1 = []
results2 = []
results3 = []

# Generowanie punktów (x,y) i sumowanie, ile z wygenerowanych punktów jest pod wykresem funkcji
for n in n_values:
    approximations1 = []
    all_points1 = []

    for _ in range(k):
        points1 = [(random.uniform(a1, b1), random.uniform(0, M1)) for t in range(n)]
        C1 = sum(1 for x, y in points1 if y <= func1(x))
        approximations1.append((b1 - a1) * M1 * C1 / n)
        all_points1.extend(points1)

    results1.append(approximations1)

for n in n_values:
    approximations2 = []
    all_points2 = []

    for _ in range(k):
        points2 = [(random.uniform(a2, b2), random.uniform(0, M2)) for t in range(n)]
        C2 = sum(1 for x, y in points2 if y <= func2(x))
        approximations2.append((b2 - a2) * M2 * C2 / n)
        all_points2.extend(points2)

    results2.append(approximations2)

for n in n_values:
    approximations3 = []
    all_points3 = []

    for _ in range(k):
        points3 = [(random.uniform(a3, b3), random.uniform(0, M3)) for t in range(n)]
        C3 = sum(1 for x, y in points3 if y <= func3(x))
        approximations3.append((b3 - a3) * M3 * C3 / n)
        all_points3.extend(points3)

    results3.append(approximations3)

# Obliczanie średnich wyników
avg_results1 = np.mean(results1, axis=1)
avg_results2 = np.mean(results2, axis=1)
avg_results3 = np.mean(results3, axis=1)

# Rysowanie wykresów, wykresy nie rysuj
#x^3
plt.figure("wykres calki z pierwiastka szesciennego z x", figsize=(10, 6))
plt.subplot(111)
plt.title("szacowana wartosc calki z pierwiastka szesciennego z x")
for i in range(len(n_values)):
    plt.scatter([n_values[i]] * k, results1[i], color='blue', marker='o', alpha=0.3)  # Punkty z każdego powtórzenia
    plt.scatter(n_values[i], avg_results1[i], color='red', marker='o')  # Średnia wyników dla danego n
plt.axhline(exact_integral1, color='green') # Dokładna wartość całki
#plt.show()

#sin(x)
plt.figure("wykres calki z sinusa x", figsize=(10, 6))
plt.subplot(111)
plt.title("szacowana wartosc calki z sinusa x")
for i in range(len(n_values)):
    plt.scatter([n_values[i]] * k, results2[i], color='blue', marker='o', alpha=0.3)  # Punkty z każdego powtórzenia
    plt.scatter(n_values[i], avg_results2[i], color='red', marker='o')  # Średnia wyników dla danego n
plt.axhline(exact_integral2, color='green') # Dokładna wartość całki
#plt.show()

#4x(1-x)^3
plt.figure("wykres calki z 4x(1-x)^3", figsize=(10, 6))
plt.subplot(111)
plt.title("szacowana wartosc calki z 4x(1-x)^3")
for i in range(len(n_values)):
    plt.scatter([n_values[i]] * k, results3[i], color='blue', marker='o', alpha=0.3)  # Punkty z każdego powtórzenia
    plt.scatter(n_values[i], avg_results3[i], color='red', marker='o')  # Średnia wyników dla danego n
plt.axhline(exact_integral3, color='green') # Dokładna wartość całki
plt.show() 