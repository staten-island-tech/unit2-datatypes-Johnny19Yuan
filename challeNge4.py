#Create a function that accepts an input and determines all factors of the number.
number = input("factor the Number: ")

factors = []

divide = (int(number) % 2)
if divide == 0:
    factors.append("2")
    factors.append(f"{divide}")
else:

print("The factors are:")
for numbers in factors:
    print(numbers)