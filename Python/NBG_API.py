#importing Libraries
import requests,json,re

#Setting URL to sent request to
url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date=2022-07-26"

#getting Response
response = requests.get(url)

#loading response into JSON
data = json.loads(response.text)

#creating Empty Dictionary
rate_convers = dict()

#iterating through JSON to get Currency codes
for item in data:
    crncy = item['currencies']
    for code in crncy:
        cd = code['code']
        rate = code['rate']
        rate_convers[cd] = rate

#input field for examle: 50USD
rawStr = input('Enter your Amt and desired currency: ')

#parsing string to get amount
rawAmt = re.findall(r'\d+', rawStr)
#number was saved into dictionary and converting it to string
s = [str(integer) for integer in rawAmt]
a_string = "".join(s)

#converting string number into int and assigning to a variable
currAmt = int(a_string)

#getting last letters to 
curname = str(rawStr[-3:]).upper()

#printing final output after performing conversion
print(currAmt * rate_convers[curname])
