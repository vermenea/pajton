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

df['Średnia'] = mean(df['Oceny'])


#zad7

df['Zdał'] = df['Oceny'] >= 3 
print(df)

#zad8

plt.plot(df['Średnia'])
plt.show()