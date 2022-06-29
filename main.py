'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
score = 0
score = int(score)

name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to Python Quiz! 
You will be presented with 5 questions.
Enter the appropriate option number to answer the question
Good luck!""".format(name))

#Question1
print("""Who developed Python Programming Language?
1. Wick van Rossum 
2. Rasmus Lerdorf
3. Niene Stom 
4. Guido van Rossum""")

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    score=score+0
else:
    
    score = score + 1

#Question2
print("""Which type of Programming does Python support?
1. object-oriented programming
2. structured programming
3. functional programming
4. all of the mentioned""")

answer2 = "4"
response2 = input("Your answer is:")

if (response2 != answer2):
    score=score+0
else:
    
    score = score + 1



#Question3
print("""What will be the value of the following Python expression?
4+3%5
1. 7
2. 2
3. 4
4. 1""")

answer3 = "1"
response3 = input("Your answer is:")

if (response3 != answer3):
    score=score+0
else:
    
    score = score + 1



#Question4
print(""" What does pip stand for python?
1. unlimited length
2. all private members must have leading and trailing underscores
3. Preferred Installer Program
4. none of the mentioned""")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    score=score+0
else:
    
    score = score + 1

#Question5
print("""Which keyword is used for function in Python language?
1. Function
2. Def
3. Fun
4. Define""")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    score=score+0
else:
    
    score = score + 1

print("Your total score is " + str(score) + " out of 5")
print("Thank you for playing, goodbye")