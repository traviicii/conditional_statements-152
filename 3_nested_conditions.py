# Nested if statements

# We can have nested if's, or if statements inside of an if statment

# Activity of the day

weather = 'sunny'
friends = 5

if weather == 'sunny': # outer condition
    # inner if's
    if friends >= 6:
        print("Let's play volleyball!!")
    elif friends == 5:
        print("Let's play frisbee!")
    else:
        if friends == 1:
            print("I think I'll play golf... all by my lonesome...")
        elif friends < 5:
            print("The", friends, "of us should play golf")
else:
    print("Let's go to the movies!")