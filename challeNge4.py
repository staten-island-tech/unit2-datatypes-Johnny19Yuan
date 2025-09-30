#Create a function that accepts an input and determines all factors of the number.
number = input("factor the Number: ")
y = number
factors = []
def division(x):
    for i in range (int(number)):
        divide = (int(number) % x)
        if divide == 0:
           factors.append(number)
           division = division - 1
        else:
           division = division - 1
division(y)


print("The factors are: ")

for numbers in factors:
    print(numbers)

#no working 💀