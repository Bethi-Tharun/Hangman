import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "development"]
    return random.choice(words)

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |
           |
           |
           |
           -
        """
    ]
    return stages[attempts]

def play_hangman():
    word = choose_word()
    guessed = set()
    attempts = 6
    correct_guesses = set()

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(display_hangman(attempts))
        print("Word: " + " ".join([letter if letter in guessed else "_" for letter in word]))
        
        if set(word).issubset(guessed):
            print("Congratulations! You've guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed.add(guess)

        if guess in word:
            print("Good guess!")
            correct_guesses.add(guess)
        else:
            print("Wrong guess!")
            attempts -= 1
        
        print("\n")

    if attempts == 0:
        print(display_hangman(attempts))
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    play_hangman()
