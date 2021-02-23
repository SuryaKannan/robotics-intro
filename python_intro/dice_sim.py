'''
MCAV JMSS - Co-Curricular 

Written by Surya Kannan
Last Modified 24/02/2021

Simple dice rolling simulator written in Python used to introduce:
- global and local variables (scope)
- print statements (debugging)
- user input (recognised as string)
- control flow (if else statments)
- data types (string, integer, float)
- lists (indexing)
- arithmetic (averaging, random)

Can progress to 
- functions (combined with switch case, reduced repetitive code)
- case/switcher statements (cover all possible combinations in a better way)
- implementing everything using OOP
'''
# import statements are used to access external libraries written by other people
# some come installed with python, such as random, however others must be installed by the user
import random 

# These are called global variables, they can be accessed and overwritten anywhere in the script
playing = True
my_bag = [] # an empty list

# This is a while loop. As long as the condition in the statement after the "while" holds, the loop will continue to run
while playing == True:
    print("\n-------------------------------------------\n")
    print("Welcome to the dice simulator!\n")
    print("-------------------------------------------\n")
    print("1: Create and add a di to my bag\n")
    print("2: Remove the most recent di from my bag\n")
    print("3: List how many dice I have and the values of all the dice in my bag\n")
    print("4: Roll all the dice in my bag and display my results\n")
    print("5: Add the face numbers of all the dice in my bag\n")
    print("6: Roll all the dice in my bag and calculate the average value\n")
    print("7: I don't like this simulator, let me get out of here!!!!\n")
    print("-------------------------------------------\n")