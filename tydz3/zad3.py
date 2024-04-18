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
