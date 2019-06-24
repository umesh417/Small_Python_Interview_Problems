n = int(raw_input())
total = 0
student_marks = {}
for _ in range(n):
    line = raw_input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = raw_input()
marks = student_marks[query_name] 
for elem in range(0, len(marks)):
    total = total + marks[elem]
    mean = total/len(marks)
    print(mean)
