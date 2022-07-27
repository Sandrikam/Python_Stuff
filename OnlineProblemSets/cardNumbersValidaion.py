import re

card = input().strip()

#filters
validNo = re.compile(r'^[456]\d{15}$').match
#isSerial = re.compile(r'')
#isGroups = 
def isCardNoValid(card):
    if len(str(card)) == 16:
        if validNo(card):
            card = re.compile(r'\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d').search
            cardNo = card.replace('-','')
            print(cardNo)
    else:
        print('Invalid')


isCardNoValid(card)

