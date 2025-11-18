# Quiz game
# Author: CyberKat123 

# We first get a tuple of questions set to variable Questions
Questions = ('How many elements are in the periodic table?: ',
             'Which animal lays the largest eggs?: ',
             'What is the most abundant gas in the atmosphere?: ',
             'How many bones are there in the human body?: ',
             'which planet in the solar system is hottest?: ')
# Next step is ,ultiple Options of possible answers, tuple too
Options = (("A. 156 ", "B. 117  ", "C. 118 ", "D. 120 "),
           ("A. Whale ", "B. Crocodile ", "C. Springbok ", "D.Ostrich "),
           ("A.Nitrogen ", "B. Oxygen ", "C. Carbon-Dioxide ", "D. Hydrogen"),
           ("A. 206 ", "B. 200 ", "C. 208 ", "D. 210 "),
           ("A.Earth ", "B.Venus ", "C.Mars ", "D.Neptune "))

# WE have a tuple of answers here 
answers = ("C", "D", "A", "A", "B")
#LIST of guesses , which we will append to the Users input guesses soon
guesses =[]
# A score at start 
score = 0
# question number is the question we are on
Question_number = 0

# For loop to print out all the questions out
for question in Questions: 
    print('--------------') # adds lines between the empty spaces between the questions
    print(question) 
     
     # Within the loop, after displaying the questions, display the options too
     # next to the questions
    for option in Options[Question_number]: #The question number variable acts as an Index
        print(option)                       #It will assign each question a number using index 
    
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess) #The answers of Udser guess will be added to the guesses list
    if guess == answers[Question_number]: 
        score += 1        # To each question
        print('Correct!')
    else: 
        print("incorrect")
        print(f'{answers[Question_number]} is the correct answer')
    Question_number += 1 

print('-----------------')
print('     RESULTS     ')
print('-----------------')


print("Answers: ", end=" " )
for answer in answers:
    print(answer , end= "" )

print ( )
print ("Guesses: ", end="")
for guess in guesses: 
    print(guess, end= "")
print()


score =int(score / len(Questions) * 100)
print(f'Your score is: {score}%')
print( )
print("Thank you for playing, come again")