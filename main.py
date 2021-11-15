#### Describe each datatype below:(4 marks)

## 4         = int
## 5.7       = float
## True      = Boolean
## Good Luck = String

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer Float

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer String


####Create a variable tha will store the users name.(1 mark)
userName = input("What is your name? ")

####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
print(userName[0:4])

####Convert the user's name to all uppercase characters and print the result
print(userName.upper())

####Find out how many times the letter a occurs in the user's name. Print the result.
print(userName.count("a"))


#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.

userAge = int(input("Enter your age:"))
if userAge < 19:
  print("You can't enter")
else:
  print("You can enter")

#### Create an empty list called squareNumbers (3 marks)
squareNumbers = []


#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, max 6 marks).
for i in range(20):
  i += 1
  squares = (i * i)
  squareNumbers.append(squares)

####Print your list (1 mark)
print(squareNumbers)

####Create a variable called userSquare that asks the user for their favourite square number
userSquare = int(input("What's your favourite square number? "))

#### Add this variable to the end of your list called squareNumbers. Print the list

squareNumbers.append(userSquare)
print(squareNumbers)


### Create a variable called choice. This variable should choose a random element from your list. You will need to import the random module. Print the variable called choice.(3 marks)

import random
choice = random.choice(squareNumbers)
print(choice)

####Create another print statement that prints the following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)

print("The random square number is, ", choice)