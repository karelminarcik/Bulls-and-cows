import random

def is_valid_guess(guess):
    """check the user input if follow predifine condition - number has to have exactly 4 digits, has to obtain only digits, cannot begin with '0' and cannot have duplicity."""
    # Check if the guess is exactly 4 characters long
    if len(guess) != 4:
        return False, "Číslo musí mít přesně 4 číslice."
    
    # Check if the guess contains only digits
    if not guess.isdigit():
        return False, "Číslo musí obsahovat pouze číslice."
    
    # Check if the guess starts with a zero
    if guess[0] == '0':
        return False, "Číslo nesmí začínat nulou."
    
    # Check for duplicate digits
    if len(set(guess)) != 4:
        return False, "Číslo nesmí obsahovat duplicitní číslice."
    
    return True, "Číslo je platné."


def secret_number():
    """create a secret number from digits 0 - 9 without digits repeating and with no '0' as a first digit."""
    
    # create a list with numbers from 0 to 9
    digits = list(range(10))
    
    # ensure that there is no 0 as a first digit
    while True: 
        # shuffle digits in the list
        random.shuffle(digits)
        if digits[0] != 0:
            break
    
    # take first 4 digit from the list
    number = ''.join(map(str, digits[:4]))
    return number



def bulls_and_cows(secret, guess_number):
    """Control if digits from 'guess_number' are obtain in 'secret'. If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows"""
    bulls = 0
    cows = 0
    for i in range(4):
        if guess_number[i] == secret[i]:
            bulls += 1
        elif guess_number[i] in secret:
            cows += 1      
    return bulls, cows



        
      
    