want_play = input("Hi. Do you want to play a game? [Yes/No]")

if want_play == "Yes":
    word = "PIANO"
    word_length = len(word)
    already_guessed = ""
    for c in word:
        already_guessed += "_"
    wrong_letters = ""
    lives = 5
    print("Guess the word. You have 5 lives")

    while lives>0:
        guessed_letter = input("Guess a letter.").upper().strip()

        if wrong_letters.__contains__(guessed_letter):
            print("You have already guessed this letter.")
            continue

        contains_letter = word.__contains__(guessed_letter)

        if contains_letter:
            letter_index = [i for i, ltr in enumerate(word) if ltr == guessed_letter]
            for i in letter_index:
                already_guessed = already_guessed[:i] + guessed_letter + already_guessed[i+1:]

            print("Correct")
            print(already_guessed)
            print("wrong letters: " + wrong_letters)
            print("Lives: " + str(lives))
            print("--------------------")

            if already_guessed.__contains__("_") == False:
                break
        else:
            lives -= 1
            wrong_letters += guessed_letter + ", "

            print("Incorrect")
            print(already_guessed)
            print("wrong letters: " + wrong_letters)
            print("Lives: " + str(lives))
            print("--------------------")

    if already_guessed.__contains__("_"):
        print("Sorry, you have lost. The correct word was " + word)
    else:
        print("You won! Congratulations :)")



