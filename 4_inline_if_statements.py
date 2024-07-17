# Inline if statments (ternary operators) are simply a way to write if statements in a single line

# syntax
# <True return> if <condition> else <False return>

candy_jar = 'emtpy'

# if candy_jar == 'full':
#     print("It's candy time!")
# else:
#     print("time to hit up Mr. Wonka")

print("It's candy time!" if candy_jar == 'full' else "time to hit up Mr. Wonka")


# ternary operator with 'and'

candy_jar = 'empty'
sweet_tooth = True

print("It's candy time!" if (candy_jar == 'full') and (sweet_tooth) else "Who needs candy anyway?")


# ternary operator with 'or'

day = 'tuesday'

print("It's the weekend!") if (day == 'saturday') or (day == 'sunday') else print("Boooooooo it's not the weekend!!")