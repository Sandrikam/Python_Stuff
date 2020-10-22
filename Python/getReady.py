import random

randomNum = random.randrange(1,5)
print(randomNum)
if randomNum==1:
    def firstFunc():
        mytext = input('Enter string ')
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = ''
        for letter in mytext:
            if letter not in vowels:
                result=result+letter
        print('modified ',result)
        print('num of consonants ',len(result))
        print('num of vowels ',len(mytext)-len(result))
        print('string size',len(mytext))
    firstFunc()
elif randomNum==2:
    def secondFunc():
        num = int(input("Enter num "))
        x=num**0.25
        if x.is_integer():
            print("good")
        else:
            print("bad")
    secondFunc()
elif randomNum==3:
    def thirdFunc():       
        mytext = input('Enter string 1 ')
        mytext1 = input('Enter string 2 ')
        if mytext == mytext1:
            print("same")
        else:
            print("not same")
        print(mytext.upper(),mytext1.lower())
    thirdFunc()
elif randomNum==4:
    def fourthFunc():
        mytext = input('Enter string ')
        space = " "
        print(mytext.count(space))
    fourthFunc()
----------------------
import random
r=random.randrange(1,5)
if r==1:
    def blacklistingi():
        s=input("text: ")
        xg=""
        xmo=0
        tan=0
        sia=[]
        for i in s:
            if i not in ["a","e","i","o","u","y"]:
                xg+=i
                tan+=1
            else:
                xmo+=1
                
        sul=xmo+tan
        sia.append (xg)
        sia.append(xmo)
        sia.append(tan)
        sia.append(sul)
                
        return sia
            
    pas=blacklistingi()
    print ("xmovnebis gareshe", pas[0],"xmovnebi: ",pas[1],"tanxmovnebi",pas[2],"sul simbolo: ",pas[3])

if r==2:            
    def rooti():
        ricxvi=int(input())
        ric=ricxvi**0.25
        k=ric
        k1=ric
        n=0
        a=4
        while a>0:
            k**=2
            a=-1
        if k==ric:
            return ("zustia")
        else:
            while k1==ric:
                k**=2
                n+=1
            return ("ar aris zusti", n)

    pas=rooti()
    print (pas)


if r==3:
    def checkingi():
        ps=[]
        s1=input("text")
        s2=input("text2")
        if s1==s2:
            p="ertnairia"
        else:
            p="ar aris ertnairi"
        ps.append(p)
        ps.append(s1.upper())
        ps.append(s2.lower())
        
        return ps

    pas=checkingi()
    print("pasuxi: ", pas[0], "didi: ", pas[1], "patara: ", pas[2])

if r==4:
    def space():
        s = input("text: ")
        return(s.count(" "), s[1:-1])

    pas=space()
    print(pas)

--
import random
randomNum = random.randrange(1,5)

print(randomNum)
if randomNum==1:
    def firstFunc():
        mytext = input('Enter string ')
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = ''
        for letter in mytext:
            if letter not in vowels:
                result=result+letter
        print('modified ',result)
        print('num of consonants ',len(result))
        print('num of vowels ',len(mytext)-len(result))
        print('string size',len(mytext))
    firstFunc()
elif randomNum==2:
    def secondFunc():
        num = int(input("Enter num "))
        x=num**0.25
        if x.is_integer():
            print("good")
        else:
            print("bad")
    secondFunc()
elif randomNum==3:
    def thirdFunc():       
        mytext = input('Enter string 1 ')
        mytext1 = input('Enter string 2 ')
        if mytext == mytext1:
            print("same")
        else:
            print("not same")
        print(mytext.upper(),mytext1.lower())
    thirdFunc()
elif randomNum==4:
    def fourthFunc():
        mytext = input('Enter string ')
        space = " "
        print(mytext.count(space))
    fourthFunc()
              
------------------
# -*- coding: utf-8 -*-
import random
randomNumber=random.randint(1,10)
if randomNumber>5:
    username=input("username ")
    password=input("password ")
    if username=="user" and password=="pass":
        print("welcome")
    elif username=="user" or password=="pass":
        print("try once more")
    else:
        print("you are hacker")
elif randomNumber<5:
    print("you are not allowed to log in")
else:
    print("you are logged in")

-----------
import random
s=input("sheiyvanet sityva ")

if s=="output":
    r1=input("ra gamoviyvano")
    r2=int(input("ramdenjer gamoviyvano"))
    print(r1*r2)
elif s=="random":
    randomNumber=random.randint(1,20)
    print(randomNumber)
elif s=="random_float":
    randomFloat=random.uniform(50,100)
    print(randomFloat)
elif s=="finish":
    print("good bye")
    
 --------
def bibl():
t=input("text: ")
s=t.split(' ')

return (s[0][0]+'.'+s[1])

print("gaiaret registracia")
str1=""
s="sworia"
while str1!=s:
sax=input("name? ")
for i in sax:
if i not in ["1","2","3","4","5","6","7","8","9","0"]:
str1="sworia"
else:
str1="arasworia" 

saxeli=sax

str2=""
s2="sworia"
while str2!=s2:
gvar=input("lastname? ")
for i in gvar:
if i not in ["1","2","3","4","5","6","7","8","9","0"]:
str2="sworia"
else:
str2="arasworia" 

gvari=gvar

asak=int(input("asaki? "))
adr=input("misamarti? ")

str3=""
s3="sworia"
while str3!=s3:
mail=input("mail? ")
for i in mail:
if i != "@":
str2="arasworia"
break
else:
str2="sworia" 

email=mail

str4=""
s4="sworia"
while str4!=s4:
parol=input("password? ")
if len(parol)!=10 or parol[1:len(saxeli)]==saxeli:
str4="arasworia"
break
else:
str4="sworia" 
password=parol

print ("please login")
m=input("email? ")
p=input("password?")
k=0
if m==email and p==password:
print ("You succesfully logged in!")
print (bibl())
elif m!=email and p!=password:
print ("arcertia swori")
else: 
while k<5:
while m!=email and password!=password:
m=input("email? ")
p=input("password?") 
if m==email and p==password:
break 
k+=1 
print("you're hacker")   

-----------1
import random

def MyFunction():
    randomNumber = random.randrange(0,2)
    count = 0
    
    if randomNumber==1:
        oldstr1 = input("Random number is 1 enter your string ")
        mystring = oldstr1.replace("a","")
        print(mystring)
        print('length of string is ',len(oldstr1))
    elif randomNumber == 0:
        oldstr0 = input("Random number is 0 enter your string ")
        for i in oldstr0:
            if (i == 'a'):
                count = count + 1
        print('this string contains ',count, ' a.')
        print('length of string is ',len(oldstr0))
    
MyFunction()
--------------------2
# -*- coding: utf-8 -*-
count=0
a = range(20)
oldstr0 = input("enter your string ")
for i in oldstr0: 
        if (i == 'b'): 
            count = count + 1
print('this string contains ',count,' b.')
if(count>5):
    print("it’s a lot")
elif(count<5):
    while(count<5):
        count=0
        oldstr0 = input("Enter your string ")
        for i in oldstr0:
            if (i == 'b'):
                count = count + 1
                if(count==5):
                    b=sum(a)
                    print('sum from 1 to 20 is ',b)
                    print('this string contains ',count,' b.')
elif(count==5):
        b=sum(a)
        print('sum from 1 to 20 is ',b)
---------3
s = input(" enter your string ")
numads = 0
for i in range(1, len(s)-1):
    if s[i:i+2] == 'ad':
        numads += 1
print ('ad occurs :',numads , ' times')
print(s[0],' ',s.partition(' ')[2])
---------------4
mytext = input('Enter string ')
vowels = ['a', 'e', 'i', 'o', 'u']
result = ''
for letter in mytext:
    if letter not in vowels:
        result=result+letter
substring = " "

count = mytext.count(substring)
print('modified ',result)
print('num of consonants ',len(result)-count)
print('num of vowels ',len(mytext)-len(result)-count+1)
print('string size',len(mytext))
-----------5
s = input('Enter string ')
r = ''
c = ''
for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char
if (len(c) > len(r)):
    r = c
print('longest substing',r)

--------------------6
word=input("Enter string ")
if  word==word[::-1]:
    print(" is palindrome")
else:
    print("is not palindrome")
