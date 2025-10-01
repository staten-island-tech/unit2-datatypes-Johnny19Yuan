#Challenge
#Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.
print ("i am the gcf calculator")
number = int(input("what is the first number? "))
number1 = int(input("what is the second number? "))

division = number
x = number
y = number1
factors = []
for i in range (int(number)):
    divide = (int(x) % division)
    if divide == 0:
       factors.append(division)
       division = division - 1
    else:
       division = division - 1

division1 = number1

factors1 = []
for i in range (int(number1)):
    divide1 = (int(y) % division1)
    if divide1 == 0:
       factors1.append(division1)
       division1 = division1 - 1
    else:
       division1 = division1 - 1

factors 