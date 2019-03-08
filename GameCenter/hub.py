print('''
----------------------------------------------------------------
''')
print('Please choose a game')
print('''[1] for blackjack (By Marco)
[2] for hangman (By Kevin)
[3] A trivia game (By RJ)
''')
choice = str(input())
if choice == '1':
    import blackjack
elif choice == '2':
    import KevinHangman
elif choice == '3':
    import RJtrivia
