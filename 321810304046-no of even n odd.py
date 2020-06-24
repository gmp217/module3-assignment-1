e,o,i=0,0,0
n=int(input("Enter no of elements:"))
print("Enter elements:\n")
while i<n:
	if(int(input())%2==0):
		e+=1
	else:
		o+=1	
	i+=1
print("Number of even :",e,"\nNumber of odd:",o)