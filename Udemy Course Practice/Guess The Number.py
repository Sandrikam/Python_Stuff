import random

print("Hey There! what's Your name?")
PlayerName = input()

if (PlayerName) == 'Tony':
  print('Fuck You Tony!')
else:
  print('Hello ' + PlayerName + ' Wanna Guess the number between 1-20?')
  secretNum = random.randint(1,20)

  for guessCount in range(1,7):
    print('Take a Guess.')
    guess = int(input())

    if guess < secretNum:
      print('Go higher!')
    elif guess > secretNum:
      print("You're high")
    else:
      break
  
  if guess == secretNum:
    print('congrats! ' + PlayerName + ' You took ' + str(guessCount) + ' Guesses')
  else:
    Print('Number was: ' + str(secretNum))
