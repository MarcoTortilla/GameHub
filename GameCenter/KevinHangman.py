import time

print ("Hello welcome to a game of hangman")
time.sleep(2)
print (" Hint: We work on it in class / A known game ")
time.sleep(2)
print ("GIVE IT YOUR BEST GUESS!!!")

import random

answerlist = ["python" , "fortnite" , "computer" ,"hangman"]

random.shuffle(answerlist)

answer = list(answerlist[0])

display = []

used = []

display.extend(answer)

used.extend(display)

for i in range (len(display)):
    display[i] = "_"

print (' '.join(display))
print()

count = 0

while count < len(answer):
    guess = input("Guess a letter: ")
    guess = guess.lower()
    print (count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count + 1
            used.remove(guess)
    if guess not in display:
      print ("WHOOPS!!! Wrong letter")


    print (' '.join(display))
    print()

print (" AYE YOU GOT THAT RIGHT!")

import hub
