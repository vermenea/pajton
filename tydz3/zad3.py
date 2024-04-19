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

def password_check():
    special_characters = string.punctuation
    while True:
        password = input("Podaj hasło:")
        if (12 <= len(password) <= 15 and 
            any(char.islower() for char in password) and 
            any(char.isupper() for char in password) and 
            any(char.isdigit() for char in password) and 
            any(char in special_characters for char in password)):
            print(f"Poprawne hasło!")
            break
        else:
            print("Hasło musi mieć pomiędzy 12 a 15 znaków i zawierać co najmniej jedną małą literę, jedną dużą literę, jedną cyfrę oraz jeden znak specjalny.")
            password = input("Podaj hasło:")

password_check()


#zad4

def fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

n = int(input("Podaj liczbę n: "))
fib_sequence = fibonacci(n)
print("Ciąg Fibonacciego:", fib_sequence)


#zad5

#zad6

def coin_flip():
    return random.choice(["orzel", "reszka"])
flips_amount = 10
print(f"Wynik: ")
for _ in range(flips_amount):
    wynik = coin_flip()
    print(wynik)

#zad7

piwa = [
    {"nazwa": "Tyskie", "kalorie_na_100ml": 43, "objetosc_ml": 500},
    {"nazwa": "Zywiec", "kalorie_na_100ml": 45, "objetosc_ml": 500},
    {"nazwa": "Lech", "kalorie_na_100ml": 42, "objetosc_ml": 330},
    {"nazwa": "Desperados", "kalorie_na_100ml": 60, "objetosc_ml": 400}
]

total_calories = 0

for piwo in piwa:
    total_calories += piwo["kalorie_na_100ml"] * piwo["objetosc_ml"] / 100
    print(total_calories)
    
#zad8

C = int(input(f"Enter celsius temperature: "))


def convert_temperature(C):
    F = 9/5 * C + 32
    return F

F = convert_temperature(C)
print(F)
    
#zad9

input_int = (input(f"Enter a few numbers to the list separated by spaces: "))
input_list = [int(num) for num in input_int.split()]
cutoff = int(input(f"Enter a cutoff number: "))

def find_numbers(input_list, cutoff):
    filtered_list_of_numbers = [num for num in input_list if num >= cutoff]
    filtered_list_of_numbers.sort()
    return filtered_list_of_numbers

result_list = find_numbers(input_list, cutoff)
print(result_list)
    
#zad10

pracownicy = {
        "87042105829": {
            "imię": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "87042105829",
            "lata_pracy":5,
            "dni_urlopu":20,
            "rola": "programista"
        },
         "920315504756": {
            "imię": "Anna",
            "nazwisko": "Nowak",
            "pesel": "92031504756",
            "lata_pracy":3,
            "dni_urlopu":25,
            "rola": "analityk"
        },
          "850110504234": {
            "imię": "Piotr",
            "nazwisko": "Wiśniewski",
            "pesel": "85010504234",
            "lata_pracy":10,
            "dni_urlopu":15,
            "rola": "HR"
        },
           "79032601235": {
            "imię": "Karolina",
            "nazwisko": "Zając",
            "pesel": "79032601235",
            "lata_pracy":7,
            "dni_urlopu":18,
            "rola": "programista"
        },    
}

def get_data():
    data = []
    info_input = input(f"Podaj dane, które chcesz uzyskać: ")
    if info_input == "imię":
        for pracownik in pracownicy.values():
            data.append(pracownik["imię"])
    elif info_input == "nazwisko":
        for pracownik in pracownicy.values():
            data.append(pracownik["nazwisko"])
    elif info_input == "pesel":
        for pracownik in pracownicy.values():
            data.append(pracownik["pesel"])
    elif info_input == "lata pracy":
        for pracownik in pracownicy.values():
            data.append(pracownik["lata_pracy"])
    elif info_input == "dni urlopu":
        for pracownik in pracownicy.values():
            data.append(pracownik["dni_urlopu"])
    elif info_input == "rola":
        for pracownik in pracownicy.values():
            data.append(pracownik["rola"])
    return data

wanted_data = get_data()           
print(wanted_data)    

#zad11


owners_pet_data = {}
clinic_pets_data = {}

def random_ID():
    return random.randint(1, 100)

def add_phone_number():
    owners_phone_number = input("Enter your phone number in the format XXXXXXXXX: ")
    while len(owners_phone_number) != 9 or not owners_phone_number.isdigit():
        owners_phone_number = input("Not valid. Please enter your phone number in XXXXXXXXX format: ")
    return owners_phone_number

def fill_not_necessary():
    answer = input("Would you like to fill in additional info? (yes or no): ") 
    if answer.lower() == "yes":
        validated_phone_number = add_phone_number()
        pets_vaccines = input("Did your pet have all necessary vaccines?: ")
        owners_pet_data["phone_number"] = validated_phone_number
        owners_pet_data["vaccines"] = pets_vaccines
    else:
        return

def fill_vet_form():
    owners_pet_data.clear() 
    pets_name = input("Enter your pet's name: ")
    pet_id = random_ID()
    pets_health_status = input("Enter what's the problem with the pet: ")

    owners_pet_data["name"] = pets_name
    owners_pet_data["id"] = pet_id
    owners_pet_data["health"] = pets_health_status
    fill_not_necessary()
    print("Thank you for filling the form!")  

    
    return owners_pet_data

def update_patients_data():
    data = fill_vet_form()
    clinic_pets_data[data["id"]] = data
    pop_up = input("Would you like to add another patient?: ")
    if pop_up.lower() == "yes":
        update_patients_data()
    else:
        print("Ok")

update_patients_data()
print("Here is updated records:", clinic_pets_data)
