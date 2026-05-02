import random

# Word list
words = ["tiger", "lion", "zebra", "panda", ",elephant"]

# Choose random word
word = random.choice(words)

# Game setup
guessed = ["_"] * len(word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

# Game loop
while attempts > 0 and "_" in guessed:
    print("\nWord (Animals):", " ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter!")
        continue

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

# Result
if "_" not in guessed:
    print("\nYou WON! The word was:", word)
else:
    print("\nGame Over! The word was:", word)
