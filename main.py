import random

# Categories with words
categories = {
    "animals": ["tiger", "lion", "zebra", "panda", "elephant"],
    "fruits": ["apple", "mango", "banana", "orange", "grapes"],
    "tech": ["python", "laptop", "server", "robot", "coding"],
    "countries": ["india", "canada", "brazil", "germany", "japan"],
    "sports": ["cricket", "football", "tennis", "hockey", "kabaddi"]
}

print("🎮 Welcome to Hangman!")

# Show categories
print("\nAvailable Categories:")
for i, cat in enumerate(categories, 1):
    print(f"{i}. {cat}")

# User selects category
choice = input("\nChoose a category: ").lower()

# Validate category
if choice not in categories:
    print("❌ Invalid choice! Defaulting to 'animals'")
    choice = "animals"

# Select random word
word = random.choice(categories[choice])

# Game setup
guessed = ["_"] * len(word)
guessed_letters = []
attempts = 6

# Game loop
while attempts > 0 and "_" in guessed:
    print(f"\nWord ({choice}):", " ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only one letter!")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong!")
        attempts -= 1

# Result
if "_" not in guessed:
    print("\n🎉 You WON! The word was:", word)
else:
    print("\n💀 Game Over! The word was:", word)
