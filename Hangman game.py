import random  # To pick a random word

# Step 1: Predefined list of words
words = ["python", "program", "hangman", "coding", "developer"]

# Step 2: Choose a random word
word = random.choice(words)
word_letters = set(word)        # Letters to guess
guessed_letters = set()         # Letters guessed
wrong_guesses = 0               # Wrong guess counter
max_guesses = 6                 # Maximum wrong guesses

print("🎮 Welcome to Hangman!")
print("_ " * len(word))  # Show underscores for each letter

# Step 3: Game loop
while wrong_guesses < max_guesses and word_letters:
    print(f"\nGuessed letters: {' '.join(sorted(guessed_letters))}")
    print(f"Wrong guesses left: {max_guesses - wrong_guesses}")

    # Show the word with guessed letters
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: ", ' '.join(display_word))

    # Step 4: Ask user for a guess
    guess = input("Guess a letter: ").lower()

    # Step 5: Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    # Step 6: Check if guessed before
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
    elif guess in word_letters:
        print("✅ Good guess!")
        guessed_letters.add(guess)
        word_letters.remove(guess)
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1
        guessed_letters.add(guess)

# Step 7: End of game
if not word_letters:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 Game Over! The word was: {word}")
