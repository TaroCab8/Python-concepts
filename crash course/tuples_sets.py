# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Create tuple
fruits = ("Apples", "Organges", " Grapes")
#fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# Single value needs trailing comma
fruits2 = ("Apple",)

# Get value
#print(fruits[1])

#Can't changes values

# Delete tuple
del fruits2


# Get length
#print(len(fruits))





# A Set is a collection which is unordered and unindexed. No duplicate members

# Create a set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Grape")

# Remove from set
fruits_set.remove("Grape")

# Clear Set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)