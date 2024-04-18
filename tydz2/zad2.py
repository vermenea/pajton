#libs
import math
import collections as col

#zad1

change_tuple = ("drzewo", "chmury", "piasek")
print(change_tuple)
change_list = list(change_tuple)
change_list.append("woda")
print(change_list)

#zad2 

a = 5**2
b = 9**2

c = math.sqrt(a + b)
print(c)

#zad3
#a
dictionary = {"name": "Natalia", "age": 23}
print(dictionary)
#b
dictionary["city"] = "Gdańsk"
dictionary["car"] = "Mercedes"
print(dictionary)
#c
dictionary["age"] = 24
print(dictionary)
#d
key, value = dictionary.popitem()
print(dictionary)
print(key, value)
#e
how_many_pairs = len(dictionary)
print(how_many_pairs)

#zad4

animal_list = ["dog", "cat", "hamster", "spider", "bunny", "bunny", "cat", "dog", "cat", "dog", "hamster", "snake", "cat", "hamster", "dog", "dog", "hamster", "chinchilla", "chinchilla", "dog", "hamster"]
how_many_times = col.Counter(animal_list)
print(how_many_times)

#zad5
students = [
    ("Adam", 1),
    ("Julia", 2),
    ("Kasia", 1),
    ("Tadeusz", 3),
    ("Ania", 2),
    ("Jan", 1),
    ("Kuba", 4)
]
lockers = col.defaultdict(list)

for student, locker_number in students:
    lockers[locker_number].append(student)

print(lockers)

#zad6 
#a
participants = [
    ("Jan Kowalski", "3A"),
    ("Elzbieta Jaworowicz", "6B"),
    ("Marek Markowski", "5C"),
    ("Juras Jurkowski", "2D"),
    ("Kasia Kowalska", "3A"),
    ("Anna Nowak", "4B"),
    ("Piotr Wiśniewski", "2D"),
    ("Magdalena Nowakowska", "2D"),
    ("Michał Kowalczyk", "6B"),
    ("Monika Lewandowska", "4B")
]
#b
resigning_participant_one = participants[2]
resigning_participant_two = participants[4]
participants.remove(resigning_participant_one)
participants.remove(resigning_participant_two)
print(participants)
#c
how_many_participants = len(participants)
print(how_many_participants)

classes = col.defaultdict(list)

for participant, class_index in participants:
    classes[class_index].append(participant)

print(classes)

count_amount_from_classes = col.Counter(class_index for _, class_index in participants)
print(count_amount_from_classes)
#d

indexes_team_A = [0, 1, 2, 3]
indexes_team_B = [7, 6, 5, 4]

team_A = []
team_B = []

for index in indexes_team_A:
    team_A.append(participants[index])

for index in indexes_team_B:
    team_B.append(participants[index])

print("Team A participants:", team_A)
print("Team B participants:", team_B)
# ja znam trochę funkcje w pythonie a nie przyszło mi nic innego do głowy niz z nich skorzystać :)

#e
team_D = col.defaultdict(list)
team_C = col.defaultdict(list)

indexes_team_D = [0, 1, 2, 3]
indexes_team_C = [7, 6, 5, 4]

for index in indexes_team_D:
    team_D["Team D"].append(participants[index])

for index in indexes_team_C:
    team_C["Team C"].append(participants[index])

print("Team D participants:", team_D["Team D"])
print("Team C participants:", team_C["Team C"])


#f
# moze podział na płci?
girls_team_indexes = [1, 3, 5, 7]     
boys_team_indexes = [0, 2, 4, 6]

boys_team = []
girls_team = []

for girl in girls_team_indexes:
    girls_team.append(participants[girl])

for boy in boys_team_indexes:
    boys_team.append(participants[boy])
    
print("Girls Team: ", girls_team)
print("Boys Team: ", boys_team)