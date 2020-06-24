i,x,y=1,int(input('Enter first number: ')),int(input('Enter second number: '))
if x>y:
 x,y=y,x
while(i<=y):
 if(x%i==0 and y%i==0):
  gcd=i
 i+=1
print("gcd:",gcd)
