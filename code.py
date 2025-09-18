"""
#intergers and floats:floats represent numbers with decimal values.
x=3
y=float(3)
print(x,y)

# lists
values=[1,2.23,5,7,2,30,15]
print(values)
for number in values:
    print(values[0])
    print(values[6])
#string:Strings are a list of characters that represent text.
count=0
x=input("input a sentence: ")
y=x.split( )
for word in y:
    count+=1
print(f"You have {count} words in you sentence")




#Booleans: we can evaluate statements to True or False never both.These are referred to as boolean data types.

day_of_the_week =input("what day is it? ")
if day_of_the_week=="friday":
    print("correct")
else:
    print("incorrect")
#F string
x="test"
print(f"hello {x}")

temp=75
if temp>68:
    print('warm')
elif temp==68:
    print('prefect')
else:
    print('cold')

"""

x=input("input a number: ")
for number in x:
    if x  2:
        print (f"Your number, {x} is even")
    elif not x  2:
        print(f"you number, {x} is odd")