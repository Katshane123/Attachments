
# Author: Cyberkat123
# Python number guessing game
import random 

lowest_num = 1 
highest_num = 100 
answer = random.randint(lowest_num, highest_num)

guesses = 0 
is_running = True 

print('Python Number guessing game')
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running: 
    guess = int(input("Enter your guess: "))
    guesses += 1
    
    if guess < lowest_num or guess > highest_num:
            print ("Number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
    elif guess < answer: 
          print ("Too low, guess again")    
    elif guess > answer:
          print  ('Too high, go lower')
    else : 
          print(f'CORRECT!! the answer was : {answer} ')
          print(f'number of guesses : {guesses}')
          is_running= False
else: 
    print("invalid guess")
    print(f"Select a number between {lowest_num} and {highest_num}")





 




     









