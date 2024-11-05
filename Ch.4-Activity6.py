#This code seperates the fruits and vegetables from a list using slicing.
Crate1 = ["Onions", "Peppers", "Mushrooms", "Apples", "Peaches"]
Crate2 = ["Lemons", "Limes", "Broccoli", "Cauliflower", "Tangerines"]
Crate3 = ["Squash", "Potatoes", "Cherries", "Cucumbers", "Carrots"]
DicingArea = [Crate1[0:3], Crate2[1:4], Crate3[0:2], Crate3[3:]]
print(f"These are the vegetables that should be taken to the dicing area: {DicingArea}")
SlicingArea = [Crate1[3:], Crate2[0], Crate2[4], Crate3[2]]
print(f"These are the fruits that should be taken to the slicing area: {SlicingArea}")