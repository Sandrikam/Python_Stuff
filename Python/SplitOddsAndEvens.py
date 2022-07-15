#odd and evens from the list
list1 = [1,2,4,5,3,6,7,9,8,10,13,15,12,14]

evens = []
odds = []

for i in list1:
  if (i % 2 == 0):
    evens.append(i)
  else:
    odds.append(i)

print('Initial List: ', list1)
print('Evens: ',evens)
print('Odds: ',odds)