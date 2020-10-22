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
