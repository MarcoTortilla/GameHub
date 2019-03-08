import random
ace = 11
cards = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumcards = 0
drawchoice = 0
drawcards = 0
equation = 21 - sumcards
affirmative = ['yes', 'Yes', 'yeah', 'Yeah', 'yup', 'Yup', 'y', 'Y', 'yea']
negative = ['No', 'no', 'Nope', 'nope', 'N', 'n', 'Nah', 'nah']

def judge(sumcards):
    if sumcards == 21:
        print('You got exactly 21! You won!!11!!!')
    elif sumcards > 21:
        print('You have went bust! Maybe next time :(')
    else:
        print('You were ' + str(int(21 - int(sumcards))) + ' away from 21 Monsiour.')

def BlckJckRecursion(sumcards):
    print('Your total sum is ' + str(sumcards))
    if sumcards > 21:
        print('You have went bust!')
    elif sumcards == 21:
        print('You have exactly 21! You won!')
    else:
        print('Will you draw?')
        print('Yes or no')
        drawchoice = input()
        if drawchoice in affirmative:
            drawcard = random.choice(cards)
            print('The card you drew was ' + str(drawcard))
            if drawcard == ace:
                if sumcards + ace > 21:
                    sumcards = sumcards + 1
                    BlckJckRecursion(int(sumcards))
                elif sumcards + 11 == 21:
                    print('You got exactly 21! You have won')
                else:
                    sumcards = sumcards + 11
                    BlckJckRecursion(int(sumcards))
            else:
                sumcards = sumcards + drawcard
                BlckJckRecursion(int(sumcards))
        else:
            judge(int(sumcards))

def blackjack():
    print('Welcome to Blackjack! Would you like to start?')
    print('Yes or no')
    start = input()
    if start in affirmative:
        print('These are your cards monsieur')
        card1 = random.choice(cards)
        card2 = random.choice(cards)
        if card1 and card2 == ace:
            card1 = 11
            card2 = 1
            print(str(card1) + ' and ' + str(card2))
            sumcards = card1 + card2
            print('Total being ' + str(sumcards))
            BlackJckRecursion(int(sumcards))
        else:
            print(str(card1) + ' and ' + str(card2))
            sumcards = card1 + card2
            print('Totalling at ' + str(sumcards))
            if sumcards == 21:
                print('''You got a blackjack! You've won monsiour!''')
            else:
                print('Your total sum is ' + str(sumcards))
                print('Will you draw?')
                print('Yes or no')
                drawchoice = input()
                if drawchoice in affirmative:
                    drawcard = random.choice(cards)
                    print('The card you drew was ' + str(drawcard))
                    if drawcard == ace:
                        if sumcards + ace > 21:
                            sumcards = sumcard + 1
                            print('Your sum is ' + str(drawcard))
                            BlckJckRecursion()
                        elif sumcards + 11 == 21:
                            print('you got exactly 21! You have won!')
                        else:
                            sumcards = sumcard + 11
                            print('The sum of your cards is now ' + str(sumcards))
                            BlckJckRecursion()
                    else:
                        sumcards = sumcards + drawcard
                        BlckJckRecursion(int(sumcards))
                elif drawchoice in negative:
                    judge(int(sumcards))
                else:
                    print('''I don't understand you mosiour.''')
                    BlckJckRecursion(int(sumcards))
    else:
        import hub


while True:
    blackjack()
    import hub
