import random as rand

HANGMAN_ASCII_ART = r"""welcome to the game hangman                                     
  _    _                                                
 | |  | |                                               
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __         
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \        
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |       
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|       
                      __/ |                             
                     |___/"""

MAX_TRIES = 6

#picture 1
PICTURE1 = """
    x-------x"""

#picture 2
PICTURE2 = """
    x-------x
    |
    |
    |
    |
    |"""

#picture 3
PICTURE3 = """
    x-------x
    |       |
    |       0
    |
    |
    |"""

#picture 4
PICTURE4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |"""

#picture 5
PICTURE5 = r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |"""

#picture 6
PICTURE6 = r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |"""

#picture 7
PICTURE7 = r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""


HANGMAN_PHOTOS = dict()
HANGMAN_PHOTOS[0] = PICTURE1
HANGMAN_PHOTOS[1] = PICTURE2
HANGMAN_PHOTOS[2] = PICTURE3
HANGMAN_PHOTOS[3] = PICTURE4
HANGMAN_PHOTOS[4] = PICTURE5
HANGMAN_PHOTOS[5] = PICTURE6
HANGMAN_PHOTOS[6] = PICTURE7

#validition functions
def check_valid_input(letter_guessed, old_letters_guessed):
    if (len(letter_guessed) > 1 or not letter_guessed.isalpha()):
        return False
    elif (letter_guessed in old_letters_guessed):
        return False
    
    return True
    
#check validation and add the guessed letter
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        if (len(old_letters_guessed) > 0):
            print(" -> ".join(sorted(old_letters_guessed)))  # Sort for readability
        return False
   
#returning the current stage of the word according to the guessings
def show_hidden_word(secret_word, old_letters_guessed):
    word = ""
    for i in range(len(secret_word)):
        if (secret_word[i] in old_letters_guessed):
            word += secret_word[i]
        else:
            word += "_"

    return word
    
#check win
def check_win(secret_word, old_letters_guessed):
    word = show_hidden_word(secret_word, old_letters_guessed)
    
    for i in range(len(word)):
        if (word[i] == "_"):
            return False
    
    return True
    
#print the appropriate stage of the hangman
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])
    
#choose secret word from given file
def choose_word(file_path, index):
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read().split()
    
    if not words:
        return None  # Handle empty file case

    index = int(index) % len(words)  # Ensure index is within bounds
    return words[index]
    
def main():
    secret_word = ""
    old_letters_guessed = []
    num_of_tries = 0
    print(HANGMAN_ASCII_ART)
    print("Number of tries: " + str(MAX_TRIES))
    file_path = input("Enter file path: ").strip().strip('"')
    file_path = file_path.replace("\\", "/")
    index = input("Enter index: ")
    secret_word = choose_word(file_path, index)
    print(secret_word)
    
    print("Let's Start")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    
    while (num_of_tries < MAX_TRIES):
        letter_guessed = input("Guess a letter: ")
        if (try_update_letter_guessed(letter_guessed, old_letters_guessed)):
            if (letter_guessed in secret_word):
                print(show_hidden_word(secret_word, old_letters_guessed))
                if (check_win(secret_word, old_letters_guessed)):
                    print("WIN")
                    break
            else:
                print("):")
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))  
        
        
    if (num_of_tries == MAX_TRIES):
        print("LOSE")
    
if __name__ == "__main__":
    main()