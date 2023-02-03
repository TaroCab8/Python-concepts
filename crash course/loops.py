# A for loop is used for iterating over a sequence ( that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sarah', 'Susan']


# Simple for loop
# for person in people:
#     print(f'Current Person: {person}')

# Break
# for person in people:
#     if person == 'Sarah':
#         break
#     print(f'Current Person: {person}')

# # Continue
# for person in people:
#     if person == 'Sarah':
#         continue
#     print(f'Current Person: {person}')


# Range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0,11):
#     print(f'Number: {i}')


# While loops execute a set of statements as lon as a condition is true

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1