# Ann Cooper
# Creating a list called sandwich_orders
sandwich_orders =['rueban','pastrami','meatball','pastrami','pastrami','club','pannini','vegetable']

# Create an empty list called finished_sandwiches
finished_sandwiches = []

print('Unfortunatly, the deli has run out of pastrami.')

# While loop to remove pastrimi from the sandwich_orders list.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through each type of sandwich, with the pop function it will take the 
# last value from teh sandwich_orders list and assign it to the variable
# sandwich. 
while sandwich_orders:
    sandwich = sandwich_orders.pop()

# Still in the while loop, print each sandwich and then add it to the 
# finished sandwich list with the append function.
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

# Now adding a heading of all the sandwiches which have been made
print('\nThe following sandwiches have been made:')

# This for loop loops through all of th finished_sandwiches and prints them
for sandwiches in finished_sandwiches:
    print(sandwiches.title())