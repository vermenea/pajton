import numpy as np

# #zad1
print("1----------------")
macierz3x2  = np.array([[1,2,3],[4,5,6]])
macierz2x3 = np.array([[1,4],[2,5],[3,6]])
print(macierz3x2)
print(macierz2x3)

# #zad2
print("2----------------")
mnozenie = np.dot(macierz2x3, macierz3x2)
print(mnozenie)

# #zad3
print("3----------------")
transp_macierz1 = macierz3x2.transpose()
transp_macierz2 = macierz2x3.transpose()
transp_macierz1_shape = np.shape(transp_macierz1)
transp_macierz2_shape = np.shape(transp_macierz2)
print(transp_macierz1)
print(transp_macierz2)
print(transp_macierz1_shape)
print(transp_macierz2_shape)

# #zad4
print("4----------------")
mnozenie_transp= np.dot(transp_macierz1, transp_macierz2)
print(mnozenie_transp)

# #zad5
print("5----------------")
i = 0
for row in transp_macierz1:
    i+=1
    print(f"Rząd: {i}: {row}")
  
# #zad6
print("6----------------")
for i, kolumna in enumerate(macierz2x3.transpose()):
    print(f"nr {i}: {kolumna}")
    
# #zad7
print("7----------------")
wynik = (macierz2x3 - macierz3x2)
print(wynik)

# #zad8
print("8----------------")
try:
    print(macierz2x3 - macierz3x2)
except ValueError:   
       print(f"ValueError occured: {ValueError}")
       print(f"Transposing data: ")
       transp = np.transpose(macierz3x2)   
finally:
       print(f"finaly")
       print(transp) 
       print(macierz2x3 - transp)

#zad9
print("9----------------")
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, sqrt): ")
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2  
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator")
            continue
        print("Result: ", result)
        
    except ValueError:
        print("Invalid input! Please enter a valid number")
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        print("bye bye")
        break

    
           
