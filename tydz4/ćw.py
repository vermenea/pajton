import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random 
from statistics import mean

file = pd.read_csv(r"/Users/vermenea/Documents/python/data.csv")

df= pd.DataFrame(file)
#zad1 #zad2
# print(df)

#zad3

df = df.sort_values('Imię')
# print(df)

#zad4

df = df.rename(columns={'Kurs_1': 'Javascript', 'Kurs_2': 'Python', 'Kurs_3': 'Java'})
# print(df)

#zad5 

grades_list = []
np.random.seed(100)

for i in range(7):
    i = random.randint(2,5)
    grades_list.append(i)

df['Oceny'] = grades_list

#zad6

df['Średnia'] = df[['Javascript', 'Python', 'Java']].mean(axis=1)



#zad7

# df['Zdał'] = df['Średnia'] >= 3 
# print(df)

#zad8

# plt.plot(df['Imię'], df['Średnia'])
# plt.xlabel('Student')
# plt.ylabel('Średnia ocen')
# plt.title('Średnie ocen studentów')
# plt.show()

#zad9

# plt.plot(df['Imię'], df['Javascript'], marker='o', linestyle='-', color='b', label='Javascript')
# plt.plot(df['Imię'], df['Python'], marker='s', linestyle='-', color='r', label='Python')
# plt.plot(df['Imię'], df['Java'], marker='^', linestyle='-', color='g', label='Java')

# plt.xlabel('Student')
# plt.ylabel('Średnia ocen')
# plt.title('Średnie ocen studentów')

# plt.legend()
# plt.show()

#zad10
# grades = ['Javascript', 'Python', 'Java', 'Oceny']
# f, axs = plt.subplots(1, 7, figsize=(25, 10), gridspec_kw={'wspace': 0.8}) 

# students = ['Anna', 'Emilia', 'Jakub', 'Marta', 'Michał', 'Piotr', 'Tadeusz']
# for i, student in enumerate(students):
#     axs[i].bar(grades, df.loc[df['Imię'] == student, grades].values[0])
#     axs[i].set_xlabel('Przedmiot')
#     axs[i].set_ylabel('Ocena')
#     axs[i].set_title(f'Oceny {student}')
#     axs[i].tick_params(axis='x', rotation=65)

# plt.show()





