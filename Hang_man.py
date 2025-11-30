# Hangman in Python 
import random
words = ("pizza" , "awards" , "university" , "gym" , "python")

#Dic of key:()
hangman_art = {0: ("    ",
                   "    ",
                   "    "),
               1: ("  O  ",
                   "    ",
                   "    "),
               2: ("  O  ",
                   "  |  ",
                   "    "),
               3: ("  O  ",
                   " /|  ",
                   "    "),
               4: ("  O   ",
                   " /|\\ ",
                   "    "),
               5: ("  O  ",
                   " /|\\  ",
                   " /  "),
               6: ("  0  ",
                   " /|\\  ",
                   " / \\ ")}

def display_man(wrong_guesses):
    print("------------------")
    for line in hangman_art[wrong_guesses]:#The key number will display man
        print(line)
    print("------------------")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():   #This contains the main body of the program
    # Variables that correspond to the Game
    answer = random.choice(words)

    hint = ['_']* len(answer)
    wrong_guesses = 0 
    guessed_letters = set()
    is_running = True 

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input')
            continue

        if guess in guessed_letters:
            print(f'{guess} is already guessed')
            continue
        
        guessed_letters.add(guess)
    
        if guess in answer: 
            for i in range(len(answer)):
                if answer [i] == guess :
                    hint[i] =  guess
        else:
            wrong_guesses = wrong_guesses + 1

        if "_" not in hint: 
            display_man(wrong_guesses)
            display_answer(answer)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_answer(wrong_guesses)
            display_answer(answer)
            print('YOU LOST')
            is_running = False 



if __name__ == "__main__":
    main()