
num = input("Enter the elements seprated by space: ")
a_list = num.split()
check = [0]
for i in a_list:
    if int(i) > check[0]:
        check.insert(0,int(i))
print(check)
