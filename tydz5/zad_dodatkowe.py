import numpy as np

#zad1
print("zad1------------------------------")
macierz1 = [[[1], [2], [3], [4], [5], [6], [7], [8], [9]]]
macierz2 = [[[10], [20], [30], [40], [50], [60], [70], [80], [90]]]

reshape_macierz1 = np.reshape(macierz1,(3, 3))
reshape_macierz2 = np.reshape(macierz2,(3, 3))
print(macierz1)
print(macierz2)
print(reshape_macierz1)
print(reshape_macierz2)

#zad2
print("zad2------------------------------")
suma = np.add(macierz1, macierz2)
roznica = np.subtract(macierz1, macierz2)
mnozenie = np.multiply(macierz1, macierz2)
dzielenie = np.divide(macierz1, macierz2)

print(f"Wynik działań: dodawanie:\n{suma}\n\nróżnica:\n{roznica}\n\nmnożenie:\n{mnozenie}\n\ndzielenie:\n{dzielenie}")

#zad3
print("zad3------------------------------")
i = 2
j = 1/2
for rzad in reshape_macierz1, reshape_macierz2:
    i += 1
    j += 1/2
    potegowanie_macierzy1 = rzad ** i
    potegowanie_macierzy2 = rzad ** j
    print(f"Macierz nr1: \n{potegowanie_macierzy1}, \nMacierz nr2: \n{potegowanie_macierzy2}")
    mnozenie = np.multiply(potegowanie_macierzy1,potegowanie_macierzy2)
    dzielenie = np.divide(potegowanie_macierzy1, potegowanie_macierzy2)
    print(f"Wynik mnożenia operacji ze sobą to: \n{mnozenie}")
    print(f"Wynik dzielenia operacji ze sobą to: \n{dzielenie}")
print("------------------------------")

#zad4
print("zad4------------------------------")
print(reshape_macierz1 ** -1)
#Integers to negative integer powers are not allowed

result = []
while True:
    try:
        user_input = int(input("Wprowadź cyfrę przez którą chcesz potęgować: "))
        for rzad in reshape_macierz1:
            temporary_results =  rzad ** user_input
            for element in rzad:
                temporary_results = element ** user_input
                result.append(temporary_results)
        print(result)
      
    except ValueError:
        if user_input == -1:
           raise(f"Nie możesz potęgować przez wartości ujemne")
        break
    
#zad5
print("zad5------------------------------")
operations = {
    'dodawanie': np.add,
    'odejmowanie': np.subtract,
    'mnożenie': np.multiply,
    'dzielenie': np.divide
}
while True:
    try:
        rows = int(input("Podaj liczbę rzędów: "))
        cols = int(input("Podaj liczbę kolumn: "))
        
        if rows <= 0 or cols <= 0:
            raise ValueError("Liczba rzędów i kolumn musi być większa niż 0!")
        
        matrix1 = np.empty((rows, cols))
        matrix2 = np.empty((rows, cols))
       
        print("Wprowadź zawartość pierwszej macierzy: ")
        for i in range(rows):
            for j in range(cols):
                matrix1[i][j] = int(input(f"Wprowadź element(liczbę) dla kolumny [{i+1}] i dla [{j+1}] rzędu: "))
                
        print("Wprowadź zawartość drugiej macierzy: ")       
        for i in range(rows):
            for j in range(cols):
                matrix2[i][j] = int(input(f"Wprowadź element(liczbę) dla kolumny [{i+1}] i dla [{j+1}] rzędu: "))
                
        print(f"Twoje macierze:\n1.{matrix1}\n\n2.{matrix2}")
        działanie = input("Jaką operację chcesz przeprowadzić na macierzach? (dodawanie, odejmowanie, dzielenie, mnożenie): ").lower()
        
        if działanie not in operations:
            raise ValueError("Niepoprawna operacja! Wybierz jedną spośród wymienionych: (dodawanie, odejmowanie, dzielenie, mnożenie)")
        
        operation = operations[działanie]
        result = operation(matrix1, matrix2)
        print(f"Wynik to:\n{result}")
        
        choice = input("Czy chcesz przeprowadzić jeszcze jakąś operację? (tak/nie): ")
        if choice.lower() == "nie":
            exit(-1)         
    except ValueError as e:
        print(f"Wystąpił błąd: {e}. Upewnij się, że wprowadzone wartości są poprawne.")