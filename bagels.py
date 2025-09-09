"""A deductive logic game where you must guess a number based on clues """
# Colors
RESET = "\033[0m"    # Reset to default color
RED = "\033[91m"     # Red text
GREEN = "\033[92m"   # Green text
YELLOW = "\033[93m"  # Yellow text
BLUE = "\033[94m"    # Blue text
MAGENTA = "\033[95m" # Magenta
CYAN = "\033[96m"    # Cyan



import random
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f'''  Bagels, a dedctive logic game.
         I am thinking of a {NUM_DIGITS} digit number with no repeated digits. 
          Try to guess what it is. Here are some clues:
When I say:         That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct 
          
For example, if the secret number was 248 
and your guess was 843, the clues would be  Fermi Pico 
'''
)
    
    while True: #Main game loop
        #This stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print('I have thought up a number. ')
        print(f'You have {MAX_GUESSES} guesses to get it.Goodluck!👍🏽')
        print("Enter 'quit' if you want to end the game and take an L ")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = '' 
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input(' > ')

                if guess.lower() == "quit":
                    print('Thanks for playing!')
                    sys.exit()
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1 
            print(f"{RED} (you have {MAX_GUESSES - numGuesses + 1} guesses left):{RESET}")
            # print(f"{RED}😢 Out of guesses! The number was {secretNum}.{RESET}")
            

            if guess == secretNum:
                print(f"{GREEN}🎉 Correct! You cracked the code!{RESET}")
                break # The player is correct, so break out of the loop.
            if numGuesses > MAX_GUESSES:
                print(f"{RED}😢 Out of guesses! The number was {secretNum}.{RESET}")
            
        # Ask player if they want to play again.
        answer = input('>').lower
        print('Do you want to play again? (yes or no)')
        if answer == "quit" or not answer.startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string mde up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order. 

    #get the first NUM_DIGITS digits in the list for the secet number:

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
      and secret number pair. """
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i]  == secretNum[i]:
            # A correct digit is in the correct place. 
            clues.append(f" \n {BLUE}Fermi: One digit is correct and in the right position.{RESET}")
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append (f"\n {YELLOW}Pico: One digit is correct but in the wrong position.{RESET}")
    if len(clues) == 0:
        return f" \n {CYAN}Bagels: No digit is correct{RESET}" # There re no correct digits at all. 
    else:
        # Sort the clues into alphabetical order so their original order 
        # doesn't give information away.
        clues.sort()
        #  Make a single string from the list of tring clues. 
        return ' '.join(clues)   

  

# If the program is run( instead of imported), run the game:
if __name__ == '__main__':
    main()





    
