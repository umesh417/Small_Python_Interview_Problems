#!/bin/bash

elem = input("enter the elements of list: ")
num = elem.split()
num = list(map(int, num))
avg = sum(num)/len(num)
print("average of num:{}".format(avg))

