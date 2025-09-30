#Create a function that accepts an input and determines all factors of the number.
number = int(input("factor the Number: "))
y = number

division = number

factors = []
for i in range (int(number)):
    divide = (int(y) % division)
    if divide == 0:
       factors.append(division)
       division = division - 1
    else:
       division = division - 1


print("The factors are: ")

for numbers in factors:
    print(numbers)