#Activity 1
name = "Pranitha"
age = 2 * 5 + 3
print(f"Hi my name is {name}. I'm {age} years old!")

#Activity 2
MagicNumber = 333
print(MagicNumber)

#Activity 3
ReyChocolateChips = 10
FinnChocolateChips = 18
print(f"Rey has less than or equal to number of chocolate chips as Finn. This is { ReyChocolateChips <= FinnChocolateChips }.")
TomChocolateChips = 50
JerryChocolateChips = "50"
print(f"Tom does not have the same number of chocolate chips as Jerry. This is { TomChocolateChips != JerryChocolateChips}.")
NeoChocolateChips = 3
TrinityChocolateChips = 3
print(f"Neo has the same number of chocolate chips as Trinity. This is { NeoChocolateChips == TrinityChocolateChips }.")
KikiChocolateChips = 30
GigiChocolateChips = 31
print(f"Kiki has less chocolate chips in her cookie than Gigi. This is {KikiChocolateChips < GigiChocolateChips}.")
BernardChocolateChips = 1010
ElsieChocolateChips = 10101
print(f"Bernard has either the same or more number of chocolate chips in his cookie. This is {BernardChocolateChips >= ElsieChocolateChips}.")

#Activity 4
GrahamCracker = 40
VanillaWafer = 64
Oreo = 20
ChocolateCaramel = 10
TripleBerry = 12
Pumpkin = 12
Apple = 10
BananaCream = 10
Mango = 12
Smores = 12
print(f"All the slices of the Chocolate Caramel Pie can be divided equally amongst the Graham Cracker lovers. This is {GrahamCracker % ChocolateCaramel == 0}.")
print(f"All the slices of the Triple Berry Pie can be divided equally amongst the Vanilla Wafer lovers. This is {VanillaWafer % TripleBerry == 0}.")
print(f"All the slices of the Mango Pie can be divided equally amongst the Graham Cracker lovers. This is {GrahamCracker % Mango == 0}.")
print(f"There will be {GrahamCracker + VanillaWafer + Oreo} people at the pie party!")

#Activity 6 (Assuming that Ada already has materials for her)
Beakers = 20
Tubes = 30
RubberGloves = 10
SafetyGlasses = 4
EnoughBeakers = Beakers/5 >= 3
EnoughTubes = Tubes/10 >= 3
EnoughRubberGloves = RubberGloves/2 >= 3
EnoughSafetyGlasses = SafetyGlasses/1 >= 3
FinalReport = f"""
Here's the final report for lab materials(not including Ada):

Each girl has enough beakers: {EnoughBeakers}
Each girl has enough tubes: {EnoughTubes}
Each girl has enough rubber gloves: {EnoughRubberGloves}
Each girl has enough safety glasses: {EnoughSafetyGlasses}
"""
print(FinalReport)

#Activity 4 (Assuming that Ada does not already have her materials yet)
Beakers = 20
Tubes = 30
RubberGloves = 10
SafetyGlasses = 4
EnoughBeakers = Beakers/5 >= 4
EnoughTubes = Tubes/10 >= 4
EnoughRubberGloves = RubberGloves/2 >= 4
EnoughSafetyGlasses = SafetyGlasses/1 >= 4
FinalReport = f"""
Here's the final report for lab materials(including Ada):

Each girl has enough beakers: {EnoughBeakers}
Each girl has enough tubes: {EnoughTubes}
Each girl has enough rubber gloves: {EnoughRubberGloves}
Each girl has enough safety glasses: {EnoughSafetyGlasses}
"""
print(FinalReport)

#Activity 7
print(12345 % 88)
print(33333333333333333333333333333 % 4269531479539)
print(95247963606313562685385324642159965432468975 % 87241366382932863)

#Activity 8
print(f"The Tripolia Galaxy has {9 ** 3} planets!")
print(f"The Deka Galaxy has {9 ** 10} planets!")
print(f"The Heptaton Galaxy has {9 ** 7} planets!")
print(f"The Oktopia Galaxy has {9 ** 8} planets!")

#Challenge: Dinner Decisions
Name = "Pranitha"
Entree = "Fried Chicken"
Side1 = "French Fries"
Side2 = "Mac n Cheese"
Dessert1 = "Chocolate Ice Cream"
Dessert2 = "Vanilla Donut"
Dessert3 = "Strawberry Ice Cream"
DinnerDecisions = f"""
Hi! My name is {Name}.
I chose {Entree} as my main meal.
To go with it, I chose {Side1} and {Side2} as my sides.
And the best part, I have {Dessert1}, {Dessert2} and {Dessert3} waiting for me for dessert!
"""
print(DinnerDecisions)