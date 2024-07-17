# Conditional Statements (if/elif/else):

### Materials needed:
- [Week 1 Day 2 Slides](https://docs.google.com/presentation/d/1UF0ifMrYy_rOf0Rm60d0vw2xnBPSGcbX/edit?usp=drive_link&ouid=112614877916387331551&rtpof=true&sd=true) from the SE Supporting Documentation 2024 folder on Google Drive
    - This will have **lots of examples to pull from**

## IF:
- W's
    - **What are they?**
        - Help our chosen coding language decide the next step when there are multiple to choose from, based on specified conditions.
    - **What do they do?**
        - Execute different blocks of code based on whether a given condition or set of conditions is true or false.
    - **Why use them?**
        - Conditional statements are powerful concepts in software engineering that allow us to create applications that perform dynamically based on gathered or changing data.
- `If` syntax and code block
```python
#Syntax
#if (condition) :
    #indent for code block
```


- Simple Conditional
```python
weather = 'rainy'

assertion = (weather == 'sunny')
print(assertion)

#-----------------#

if weather == 'sunny': #check a conditon or assertion
    print('Lets have a picnic!') #run this code if conditon is true

torch_lit = True

if torch_lit:
    print("My path is clear!")
```

- Two conditions using the `and` operator
```python
#COMPOUND CONDITIONALS USING 'and' and 'or' logical operators

#--- and : requires that both conditons are True in order to execute our code block

gold_coins = 10
silver_coins = 50

if gold_coins > 5 and silver_coins > 30:
    print("Enough to buy the magic potion!")
```
- Two conditions using the `or` operator
```python
#--- or: requires that at least one condition needs to be True to execute the code block

day = 'Monday'

if day == 'Saturday' or day == 'Sunday': #as long as the day is either saturday or sunday
    print('YAYYYYY its the weekend!') # run our code block

#--- Using 'and' and 'or' TOGETHER

caffinated = True
prepared_lvl = 11
confidence = 60

#how ready am I to teach
if caffinated and prepared_lvl > 6 or confidence >= 80:
    print('IM REAAADDDDYYYY to teach!')
```

- Not conditions using the `not` operator or `!=`
```python
#--- Using 'not' logical operator

#By incorporating 'not' our if statement runs off of False conditions


busy = False

if not busy:
    print('Ahhhh time to relax!')


time = 8.30

if not time < 7:
    print('I should be awake!')
```
 
- Greater or lesser than conditions
- Checking ranges/between `(10 <= target <= 20)`

## Understanding the If Elif Else chain:
- `If` is the original condition, and you can add one or more additional conditions using `elif`.
    - `elif` connects to the previous `if` statement. Otherwise, individual `if` statements are their own "code block."
- This chain is read top-down; once one condition evaluates to true, its code block is executed, and the rest of the conditions are skipped.
- If none of your conditions are met, you can have a default condition called `else` that sits at the end of the chain and runs if none of the conditions before it evaluate to true.

```python
#If statements are our original condition
# Elif allows us to chain on additonal conditions/assertions, with corresponfing
#code blocks to 

#the flow of the if elif chain is top down, and as soon as a conditon evaluates
# to true that coee block is ran and the rest of the condtions are skipped

money = 15


if money >= 50:
    print('Lets have a nice steak dinner')
elif money >= 20:
    print('Italian sounds like a good choice!')
elif money >= 10:
    print('Lets grab chipotle!')

#Else statements, essentially a default condtion. They dont have a specific condition of their own
#but if none of the other conditions evaluate to True, than the else code block runs

#you'll only have one else per if chain
# it will always be at the very end

money = 8

if money >= 50:
    print('Lets have a nice steak dinner')
elif money >= 20:
    print('Italian sounds like a good choice!')
elif money >= 10:
    print('Lets grab chipotle!')
else:
    print("I probably should just cook at home :(")
```


### Nested If’s:
- Nested conditions
- Conditions inside conditions

```python
#In python we can have nested if's, or if statements inside if statements

#Activity of the day

#nested ifs allow us to check conditions based on another condition being true
#inner ifs are dependent on outer condition being true

weather = 'cloudy'
friends_and_i = 2

if weather == 'sunny': # outter condition
    #inner ifs 
    if friends_and_i >= 6:
        print('Lets play vollyball')
    elif friends_and_i == 5:
        print('Lets play frisbee')
    else:
        if friends_and_i == 1:
            print('I think Ill play some golf...all by my lonesome :(')
        else:
            print('The', friends_and_i, 'of us, should play golf!')
else:
    print('Lets go to the movies')
```


### Inline If’s/Ternary Operator:
- Syntax
- `<True return> if <condition> else <False return>`
- Checking between a range
- Using `and`
- Using `not`

```python
#Inline if statements aka Ternary Operators are simply a way to write if statements
#in a single line

#Syntax
#if_output if (condition) else else_output

#Why? allows to have concise conditionals within a single line

candy_jar = 'empty'

print('Its Candy Time!' if candy_jar == 'full' else 'Time to hit up Mr. Wonka!')

#ternary operator with 'and'

candy_jar = 'empty'
sweet_tooth = True

print('Its Candy Time!' if candy_jar == 'full' and sweet_tooth else 'Who needs candy anyway')

#ternary operator with 'or'

day = 'Tuesday'
print('Its the weekend') if day == 'Saturday' or day == 'Sunday' else print('BOOOOOOOOO its the work week')
```

### Pass: 
`Pass` is a temporary stand-in while you don’t yet have the logic for a code block.

```python
#Pass statement is a placeholder key word, or temporary standin for codeblocks
feeling = 'great'

#Allows us to intentionally leave things blank, as to not cause errors

if feeling == 'sick':
    pass
elif feeling == 'decent':
    pass
elif feeling == 'good':
    pass
else:
    print('Wow Im feeling GREAT lets go running')
```


### Examples: 
Do a couple of examples in VSCode, and then just reference the setup from the slides (no need to write them all out).