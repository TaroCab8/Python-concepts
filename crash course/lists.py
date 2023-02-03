# A List is a collection which is ordered and changeable. Allows duplicate members. Like arrays in js

#Create List

numbers = [1,2,3,4,5]
fruits = ["Apple", "Oranges", "Grapes", "Pears"]

#create through constructor
numbers2 = list((1,2,3,4,5))

#print(numbers, numbers2)

# Get a Value
print(fruits[1])

#Get length

print(len(fruits))

#Append to List

fruits.append("Mangos")

#Remove from list
fruits.remove("Grapes")

# Change value
fruits[0] = "Blueberries"

#Insert into position
fruits.insert(2, "Strawberries")

# Remove with pop
fruits.pop(2)

#reverse List
fruits.reverse()

#Sort List
fruits.sort()

#reverse sort
fruits.sort(reverse=True)