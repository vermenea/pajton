import numpy as np

#zad1
macierz1 = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
macierz2 = [[10], [20], [30], [40], [50], [60], [70], [80], [90]]

reshape_macierz1 = np.reshape(macierz1,(3, 3))
reshape_macierz2 = np.reshape(macierz2,(3, 3))
print(macierz1)
print(macierz2)
print(reshape_macierz1)
print(reshape_macierz2)

#zad2

suma = np.add(macierz1, macierz2)
roznica = np.subtract(macierz1, macierz2)
mnozenie = np.multiply(macierz1, macierz2)
dzielenie = np.divide(macierz1, macierz2)

print(f"Wynik działań: dodawanie:\n{suma}\n\nróżnica:\n{roznica}\n\nmnożenie:\n{mnozenie}\n\ndzielenie:\n{dzielenie}")