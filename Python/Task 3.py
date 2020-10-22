string = input("enter the word you desire: ")
numAds = 0
ltrCount = input("letters you want to count")
for i in range(1,len(string)-1):
    if string[i:i+2] == ltrCount:
        numAds +=1
print(ltrCount + 'Occurs: ',numAds,'times')
print(string[0],'',string.partition(' ')[2])
    