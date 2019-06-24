
num = int(input("Enter the number"))
a=[]
for i in range(2,num+1):
    if(num%i==0):
        a.append(i)
a.sort()
print(a[0])
 
