# Pass statement is a placeholder keyword, or temporary standin for a codeblock

feeling = 'decent'

if feeling == 'sick':
    pass
elif feeling == 'decent':
    pass
elif feeling == 'good':
    pass
else:
    print("Wow, I'm feeling great, let's go running!")

#----------------------#

user_input = input("Where do you wanna go next?")

if user_input == 'cave':
    pass # expand on options for cave exploration
elif user_input == 'left fork':
    user_input = input("Explor the woods? or continue down the road")
    if user_input == 'woods':
        pass
    elif user_input == 'continue':
        pass 
elif user_input == 'lake':
    pass # what happens at the lake?
else:
    print("choose a valid option")