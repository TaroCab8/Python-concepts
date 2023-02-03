# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. Similar to obj in js.

# Create a dict

person = {
    'first_name': "John",
    'last_name': "Doe",
    'age': 30
}

#print(person, type(person))

# Use Constructor
#person2 = dict(first_name="Sarah", last_name="Ozaki")

# Get Value
#print(person['first_name'])
##print(person.get('last_name'))

# Add key/value
person['phone'] = "555-555-555"

#print(person)

# Get dict keys
#print(person.keys())

# Get dict items
#print(person.items())

# Copy dict

person2 = person.copy()
person2['city'] = "Boston"



# Remove item

del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()

# Get lengh

#print(len(person))

# list of dict
people = [
    {'name': "Martha", 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)