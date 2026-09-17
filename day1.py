a= int(input("enter first number:"))
b= int(input("enter second number:"))
c= int(input("enter third number:"))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")




n= int(input("enter a number:"))
if(n%2==0):
    print("even")
else:
    print("odd")





d= int(input("enter a number:"))
count=0
for i in range(1,d+1):
    if(d%i==0):
        count+=1
if(count==2):
    print("prime")
else:
    print("not prime")




e= int(input("enter a number:"))
fact=1
for i in range(1,e+1):
    fact=fact*i
print("factorial is:",fact)


n=int(input("enter a number:"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c



n=int(input("enter a number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("Reverse is:",reverse)


num=int(input("Enter a number"))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")