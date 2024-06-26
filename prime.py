n=int(input("Enter a number"))
f=0
for i in range(2,n):
    if(n%i==0):
        f=f+1
        break
if(f>0):
    print("The given number",n,"is not a prime number")
else:
    print("The given number",n,"is  a prime number")