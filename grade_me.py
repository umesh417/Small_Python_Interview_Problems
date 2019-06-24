#!/bin/python3

n = input("enter the numbers..")
n = n.split()
total = 0
for elem in n:
    total = int(elem) + total
score = (total/(100*len(n))
print(score)
#if(avg>=90):
#    print("Grade: A ")
#elif(avg>=80&avg<90):
#    print("Grade: B ")
#elif(avg>=70&avg<80):
#    print("Grade: C")
#elif(avg>=60&avg<70):
#    print("Grade: D")
#else:
#    print("Grade: F")

