"""def factors(x,y):
    if x % y == 0:
        print ("factor")
factors(20,5)

i=0
while i<5:
    print(i)
    i +=1

x=int(input("give me a number i will find the factors for it: "))
y=1
prin=False
while y<=x:
    if x%y==int():
        prin=True
    y+=1
y-=1
if prin:
    print(f"factor:{y}")"""


x=int(input("give me a number i will find the factors for it: "))
y=1
factors=[]
while y<=x:
    if x%y==int():
        factors += [y]
    y+=1
print(f"factors:{factors}")