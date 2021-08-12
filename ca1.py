# name = input("Hello what is your name? ")
# print("Hello, " + name + ", time to play hangman!")
# print("Start guessing...")
underscore = ""
secret_word = input("Player 1, what is your secret word? ")
for i in range(len(secret_word)):
    underscore += "_  "
print(underscore)
array1 = list(secret_word)
guess = []
turns = 10
stringSum = ""
arraySum = [""] * len(secret_word)
objectMe = 0
print(arraySum)
for i in range(len(secret_word)):
    letter = input("Player 2, what is your letter? ")
    guess.append(letter)
    for q in range(len(secret_word)):
        if guess[i] == array1[q]:
            objectMe = guess[i]
            arraySum[q] = objectMe

        elif guess[i] == "_":
            objectMe = "_"
            arraySum[q] = objectMe

    print(arraySum)
print("Secret word: " + str(array1))
print("Your guess: " + str(guess))
for i in range(len(secret_word)):
    if guess[i] == array1[i]:
        stringSum += array1[i] + " "

print("You got " + stringSum + "correct")
