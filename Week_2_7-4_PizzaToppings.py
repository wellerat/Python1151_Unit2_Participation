# Ann Cooper

# Created a variable and assigned it a value to allow the first execution of the 
# while loop
toppings = "";

# The prompt is just a variable with the value of a string, but makes the code 
# in the while loop easier to read.
prompt = "\nPlease type a pizza topping for your pizza, if you are done type quit:  "

# This while loop will run until the string 'quit' has been entered in the prompt.
# This is case sensitive.  When the user enters 'quit' the while loop will not 
# execute again, but the current while loop will finish.
while toppings != 'quit':
    #  The input function allows user input, and in this case assigns it to the 
    # variable toppings
    toppings = input(prompt)
    # Then topping is evaluated against the string 'quit'.  If it is 'quit' the 
    # else statement will print
    if toppings != 'quit':
        print(f"I will add {toppings} to your pizza")
    else:
        print(f"Thank you for ordering your pizza")


