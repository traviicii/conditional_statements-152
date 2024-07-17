# If statement is our original condition
# elif allows us to chain additional conditions/assertions, with their own corresponding code blocks

# the flow of the if/elif chain reads from top down, and as soon as a conditional statement evaluates to True, that code block and the rest of the conditions are skipped

money = 75

if money >= 50:
    print("We can have a steak dinner!")
elif money >= 20:
    print("Italian sounds like a good choice")
elif money >= 10:
    print("Let's grab some Chipotle!")

# if money >= 10:
#     print("Let's grab some Chipotle!")
# elif money >= 20:
#     print("Italian sounds like a good choice")
# elif money >= 50:
#     print("We can have a steak dinner!")

#---------#
# Else statements are essentially a default condition
# They don't have a specific condition of their own, if none of the other conditions evaluate to True, then the else block will run it's code

money = 8

if money >= 50:
    print("We can have a steak dinner!")
elif money >= 20:
    print("Italian sounds like a good choice")
elif money >= 10:
    print("Let's grab some Chipotle!")
else:
    print("Maybe I should just cook at home... :(")