NumberList1 = [1, 2, 3, 4]
NumberList2 = [1, 2.0, 3, 4]
print(NumberList1 == NumberList2)
Fruits = ["Mango", "Watermelon", "Oranges", "Raspberries", "Blueberries"]
print(Fruits[2])
print(Fruits[1:4])
print(Fruits[1:])
Fruits = Fruits + ["Jackfruit", "Guava"]
print(Fruits)
IsValid = "Mango" not in Fruits
print(f"Pranitha likes mango: {IsValid}")
Fruits.append("Apple")
print(Fruits)
Fruits.remove("Guava")
print(Fruits)
del Fruits[2]
print(Fruits)
Fruits[3:3] = ["Apple"]
print(Fruits)