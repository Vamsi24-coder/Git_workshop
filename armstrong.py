
n=int(input("Enter a number"))
a=n
b=n
c=0
sum=0
while(a!=0):
    a=int(a/10)
    c=c+1
while(b!=0):
    r=b%10
    sum = sum + r**c
    b=int(b/10)
if(sum==n):
    print("The given number",n,"is a palindrome")
else:
     print("The given number",n,"is not a palindrome")
