# If statements

# syntax
# if (condition):
#     indent for code block

weather = 'rainy'

assertion = (weather == 'sunny')
print(assertion)

#--------------#

if weather == 'sunny': # if statements are always looking for a True condition/assertion
    print("Let's have a picnic!")

torch_lit = True

if torch_lit:
    print("My path is clear")

if True:
    print("this will always run because this condition is literally true all the time")

#-----------------------------#

# user_input = input("Would you like to explore the cave or continue down the spooky path?")

# if user_input == 'cave':
#     print("Oooooh you just entered a dark cave!!")
# elif user_input == 'spooky path':
#     print("This path is spooky but you bravely charge forward")
# else:
#     print("enter a valid option!")

# If statements check for a True condition/assertion, if it's True will execute a defined code block

#----------------------#

# COMPOUNT CONDITIONAL STATEMENTS using 'and', and 'or' logical operators

#--- and : requires both conditions are True in order to execute the indented code block

gold_coins = 10
silver_coins = 50

if (gold_coins >= 5) and (silver_coins >= 30):
    print("Enough to buy the magic potion!!")


# or : Requires that at least one condition needs to be True in order for our code block to run

day = 'monday'

if (day == 'saturday') or (day == 'sunday'):
    print("Yaaaaaaay it's the weekend!!")

# print(bool(''))

if (day == 'monday') or (day == 'tuesday') or (day == 'wednesday'): # could continue chaining on more conditions if you want
    print("Aww man it's a weekday...")

#----------------#

# Using 'and' and 'or' TOGETHER

caffinated = True
prepared_lvl = 5
confidence = 70

# How ready am I to teach?
        # True          # False
if (caffinated and prepared_lvl > 6) or (confidence > 80):
    print("I'M READYYYYYYYY TO TEACH!!!")
else:
    print("Oh no I'm not ready yet!!!")


dressed = True
weather = 'rainy'
num_of_friends = 4

if (dressed and num_of_friends > 3) or (weather == 'sunny'):
    print("Let's go to the beach!!!")

print(dressed and num_of_friends > 3)
print(weather == 'sunny')

#--- using the 'not' operator

# By incorporating 'not' our if statements can now check for False conditions

busy = False

# if not True
if not busy:
    print("Nice! time to relax!")

# if False:
#   run code

time = 8.30

if not (time < 7):
    print("I should be awake!")

if time > 7: # this is literally the same thing, just less complicated
    print("I should be awake!!!!!!!")

# there's usually a way to work around having to use 'not'