import pandas as pd

#zad1
data_frame = pd.read_excel("/Users/vermenea/Documents/python/ceny_gier.xlsx")
# print(data_frame)

def search():
    minimum = 999999999999
    for cena in data_frame["cena"]:
        if cena <= minimum:
            minimum = cena 
    cheapest_game = minimum
    game = data_frame["gra"][7]
    print(f"Cheapest game is {game} and it costs: {cheapest_game}")

if __name__ == "__main__":
    search()
    
#zad2,#zad4

class Human:
    def __init__(self,name, surrname, age, height, weight):
        self.name = name
        self.surrname = surrname
        self.age = age
        self.height = height
        self.weight = weight
    
    def go_to_shop():
        return  f"idź"
    
    def buy_for_lowest_price():
        cheap_game = search()
        return f"{cheap_game}"

# insert = input("Tell me your name: ")
# first_human = Human(insert,"coś", 12,252,12)
# first_human.name = insert   
# print(first_human.name)


# print(Seba.name)
# print(Seba.surrname)
# print(Seba.age)


#zad3

Seba = Human("Seba", "Jakiś", 25, 167, 70)
Jula = Human("Jula", "Jakaś", 20, 157, 48)       
    
#zad5
    
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2 
           
#zad6
#a)
kalk = Calculator(5, 3)
print(kalk.add())
#b)
kalk = Calculator(64,29)
print(kalk.substract())
#c)
kalk = Calculator(7,9)
print(kalk.multiply())
#d)
kalk = Calculator(8,0)
# print(kalk.divide())

#f) todo
#g) todo

#zad7*