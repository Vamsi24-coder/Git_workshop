n=int(input("Enter a numnber"))
x=n
sum=0
while(x!=0):
   r=x%10
   sum=sum*10+r
   x=int(x/10)
if(sum==n):
   print("Given number is palindrome")
else :
   print("Given number is not a palindrome")
