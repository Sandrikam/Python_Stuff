from collections import Counter
my_str = input("Enter a Word: ")
count = my_str.count("b")
print (count)

if count > 5:
    print("That's a Lot! ")
    
else:
    my_str=input("Enter string again! ")
        