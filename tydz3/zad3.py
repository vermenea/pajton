#lubs
import string
import random

#zad1
studenci = {
    "001": {
        "imie_nazwisko":"Katarzyna Nowak",
        "numer_indeksu":"123456",
        "punkty":84
    },
     "002": {
        "imie_nazwisko":"Piotr Kowalski",
        "numer_indeksu":"234567",
        "punkty":76
    },
      "003": {
        "imie_nazwisko":"Anna Zieba",
        "numer_indeksu":"345678",
        "punkty":45
    },
       "004": {
        "imie_nazwisko":"Marek Jankowski",
        "numer_indeksu":"456789",
        "punkty":59
    },
        "005": {
        "imie_nazwisko":"Ewa Maj",
        "numer_indeksu":"567890",
        "punkty":97
    }
}

for numer in studenci:
    punkty = studenci[numer]["punkty"]
    if punkty > 95:
        studenci[numer]["ocena"] = 5
    elif punkty > 80:
        studenci[numer]["ocena"] = 4
    elif punkty >= 60:
        studenci[numer]["ocena"] = 3
    elif punkty >= 50:
        studenci[numer]["ocena"] = 2
    else:
        studenci[numer]["ocena"] = 1
print(studenci)

#zad2

dany_rok = 2024

if (dany_rok % 4 == 0 and dany_rok % 100 != 0) or (dany_rok % 400 == 0):
     print(f"{dany_rok} jest przestępnym rokiem")
else:
     print(f"{dany_rok} nie jest przesępnym rokiem")



#zad3

# def password_check():
#     special_characters = string.punctuation
#     while True:
#         password = input("Podaj hasło:")
#         if (12 <= len(password) <= 15 and 
#             any(char.islower() for char in password) and 
#             any(char.isupper() for char in password) and 
#             any(char.isdigit() for char in password) and 
#             any(char in special_characters for char in password)):
#             print(f"Poprawne hasło!")
#             break
#         else:
#             print("Hasło musi mieć pomiędzy 12 a 15 znaków i zawierać co najmniej jedną małą literę, jedną dużą literę, jedną cyfrę oraz jeden znak specjalny.")
#             password = input("Podaj hasło:")

# password_check()


#zad4

# def fibonacci(n):
#     fibonacci_sequence = []
#     a, b = 0, 1
#     while len(fibonacci_sequence) < n:
#         fibonacci_sequence.append(a)
#         a, b = b, a + b
#     return fibonacci_sequence

# n = int(input("Podaj liczbę n: "))
# fib_sequence = fibonacci(n)
# print("Ciąg Fibonacciego:", fib_sequence)


#zad5

#zad6

# def coin_flip():
#     return random.choice(["orzel", "reszka"])
# flips_amount = 10
# print(f"Wynik: ")
# for _ in range(flips_amount):
#     wynik = coin_flip()
#     print(wynik)

#zad7

# piwa = [
#     {"nazwa": "Tyskie", "kalorie_na_100ml": 43, "objetosc_ml": 500},
#     {"nazwa": "Zywiec", "kalorie_na_100ml": 45, "objetosc_ml": 500},
#     {"nazwa": "Lech", "kalorie_na_100ml": 42, "objetosc_ml": 330},
#     {"nazwa": "Desperados", "kalorie_na_100ml": 60, "objetosc_ml": 400}
# ]

# total_calories = 0

# for piwo in piwa:
#     total_calories += piwo["kalorie_na_100ml"] * piwo["objetosc_ml"] / 100
#     print(total_calories)
    
#zad8

# C = int(input(f"Enter celsius temperature: "))


# def convert_temperature(C):
#     F = 9/5 * C + 32
#     return F

# F = convert_temperature(C)
# print(F)
    
#zad9

# input_int = (input(f"Enter a few numbers to the list separated by spaces: "))
# input_list = [int(num) for num in input_int.split()]
# cutoff = int(input(f"Enter a cutoff number: "))

# def find_numbers(input_list, cutoff):
#     filtered_list_of_numbers = [num for num in input_list if num >= cutoff]
#     filtered_list_of_numbers.sort()
#     return filtered_list_of_numbers

# result_list = find_numbers(input_list, cutoff)
# print(result_list)
    
#
