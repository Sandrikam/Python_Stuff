import requests,json,re

url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date=2022-07-26"

response = requests.get(url)

data = json.loads(response.text)

rate_convers = dict()

for item in data:
    crncy = item['currencies']
    for code in crncy:
        cd = code['code']
        rate = code['rate']
        rate_convers[cd] = rate

rawStr = input('Enter your Amt and desired currency: ')

rawAmt = re.findall(r'\d+', rawStr)
s = [str(integer) for integer in rawAmt]
a_string = "".join(s)

currAmt = int(a_string)
#rawStrrex = re.compile(r'\w\w\w+')

curname = str(rawStr[-3:]).upper()

#print(curname, currAmt)
print(currAmt * rate_convers[curname])
