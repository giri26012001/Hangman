word_list = ["camel", "goat", "dog", "car", "bmw", "horse", "cat", "elephant"]
import random
lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letter = []
while not game_over:
    print(f'You have{lives}/6 lifes left')
    guess = input("guess a letter: ").lower()
    if guess in chosen_word:
        print(f"You have guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f'You have guessed {guess} which is not in the word. You loose a life.')
        if lives == 0:
            game_over = True
            print(f"{chosen_word} is the correct word.You lose")
    if "_" not in display:
        game_over = True
        print("You win")
    print(hangman[lives])
