student = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    cls = [name,score]
    student.append(cls)


#print(student[0][1])
#marks = []
#for i in range(len(student)):

marks = []    
for i in student:
    j = student.index(i)
    marks.append(student[j][1])
    if (j == len(student) - 1):
        max_marks = max(marks)
        for i in student:
            print(student[j][0]) if (student[j][1] >= max_marks)


#    if (j == len(student) - 1):
#        max_marks = max(marks)
#        if student[j][1] >= max_marks:
#            print(student[j][0])
#            break
#        else:
#            pass 
#    else:
#        print("I am not there...")    
#    while j>0:
#        if student[j][1] > student[j-1][1]:
#            student[j-1], student[j] = student[j], student[j-1]
#            marks.append(student[j-1][1])
#        else:
#            break
#        j = j-1 
#print(student)
#print(marks)
#    print(student[i][i+1])
#    print(i)
#    print("alla halla lol")
#    print(i+1)
#    if (student[i][1] > student[i+1][1]):
#        marks.append(student[i][1])
#    elif (student[i][1] == student[i+1][1]):
#        marks.append(student[i][1])
#        marks.append(student[i+1][1])
#    else:
#        marks.append(student[i+1][1])

#print(marks)
    
    
