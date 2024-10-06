#This decides what breakfast for each day of the week
DaysOfTheWeek = ["Upma", "Pongal", "Pasta", "Idly", "Dosa", "Idiappam", "Cornflakes"]
Today = "Thursday"
if Today == "Monday":
    print(DaysOfTheWeek[1])
elif Today == "Friday":
    print(DaysOfTheWeek[4])
if Today == "Sunday":
    print(DaysOfTheWeek[0])
elif Today == "Saturday":
    print(DaysOfTheWeek[7])
if Today == "Tuesday":
    print(DaysOfTheWeek[3])
elif Today == "Thursday":
    print(DaysOfTheWeek[5])
if Today == "Friday":
    print(DaysOfTheWeek[6])    