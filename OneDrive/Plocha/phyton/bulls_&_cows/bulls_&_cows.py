"""

bulls_&_cows.py: druhy projekt do Engeto Online Python Akademie

author: Karel Minarčík

email: k.minarcik@seznam.cz

discord: Karel Minarčík | karlos9957

"""

from my_functions import secret_number, is_valid_guess, bulls_and_cows

# Getting value for high score if exists
try:
    with open("high_score.txt") as data:
        high_score = int(data.read())
except (FileNotFoundError, ValueError):
    high_score = float('inf')  # Use infinity as a default high score
    
secret = secret_number()
attempts = 0

print(
    """
__________      .__  .__             ____    _________                      
\______   \__ __|  | |  |   ______  /  _ \   \_   ___ \  ______  _  ________
 |    |  _/  |  \  | |  |  /  ___/  >  _ </\ /    \  \/ /  _ \ \/ \/ /  ___/
 |    |   \  |  /  |_|  |__\___ \  /  <_\ \/ \     \___(  <_> )     /\___ \ 
 |______  /____/|____/____/____  > \_____\ \  \______  /\____/ \/\_//____  >
        \/                     \/         \/         \/                  \/ 

    """
)

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
# checking if high score has already been written.
if high_score == float('inf'):
    print("There is no high score yet.")
else:
    print(f"The high score is: {high_score}")
print("-----------------------------------------------")
while True:
        guess = input("Enter a number: ")
        valid, message = is_valid_guess(guess)

        
        if valid:
            attempts += 1
            bulls, cows = bulls_and_cows(secret, guess)
            print(f"{bulls} Bulls, {cows} Cows")
            print("-----------------------------------------------")
            if bulls == 4:
                print(f"Congratulations! You guessed the correct '{secret}' number in {attempts} attempts.")
                if attempts < high_score:
                    with open("high_score.txt", mode="w") as data:
                        data.write(f"{attempts}")
                print(f"You have reached a new high score : {attempts}")
                break
        else:
            print(f"Error: {message}")
            print("Try it again.")
            

    
