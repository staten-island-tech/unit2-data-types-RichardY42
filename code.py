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



x=input("input a number: ")
value=int(x)
if value % 2 == int():
    print (f"Your number, {x} is even")
else:
    print(f"you number, {x} is odd")
#yeaaaasssasasasasasssssssssssszaaaaaaaaaaaas



x= float(input("enter your bill: "))
print(x)
y= input("select a tip of either 0 percent, 15 percent, 20 percent, or 25 percent: ")
a=x+x*0.15
b=x+x*0.20
c=x+x*0.25
if y == "0":
    print(f"total:{x}")
if y == "15":
    print(f"total: {a}")
if y == "20":
    print(f"total: {b}")
if y =="25":
    print(f"total: {c}")



x=int(input("give me a number i will find the factors for it: "))
y=1
while y<=x:
    if x%y==int():
        print(f"factor:{y}")
    y+=1

"""

no1= int(input("give me a number: "))
no2= int(input("give me another number: "))
x=1
while 
    if no1>no2:
        for i in range(no1):
            x+=1
    elif no2>no1:
        for i in range(no2)
            x+=1
if no1 % x