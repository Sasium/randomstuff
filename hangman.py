import random
list_of_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(list_of_words)
print('H A N G M A N')
while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == "exit":
        break
    if option == "play":
        letters_set = set(word)
        shadowed_string = list("-" * len(word))
        count = 0
        guess = 0
        used_letters_set = set()
        while count < 8:
            print()
            print("".join(shadowed_string))
            letter = input("Input a letter: ")
            used_letters_set.update(shadowed_string)
            if len(letter) > 1:
                print("You should input a single letter ")
            elif not letter.islower():
                print("It is not an ASCII lowercase letter")
            elif letter in used_letters_set:
                print("You already typed this letter")
            elif letter in letters_set:
                for i in range(len(shadowed_string)):
                    if word[i] == letter:
                        shadowed_string[i] = letter
                if "-" not in shadowed_string:
                    print("You guessed the word!")
                    print("You survived!")
                    print()
                    break
            else:
                print("No such letter in the word")
                used_letters_set.add(letter)
                count += 1
        if count == 8:
            print("You are hanged!")
            print()
