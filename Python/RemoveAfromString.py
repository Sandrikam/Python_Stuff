import random
for r in range(1):
  rand = random.randint(0,1)
  print(rand)
  word = input("enter word: ")
if rand> 0  :

  print(word.replace('a',''),len(word))
elif 'a' in word:
  print('yas',len(word))
else:
  print(len(word))