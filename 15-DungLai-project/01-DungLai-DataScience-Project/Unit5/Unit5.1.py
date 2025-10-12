#read file
with  open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

#remove last student (empty student)
students.pop()

#split header
header = header.split(",")
subject = header[5:]

total_student = len(students)

#split each student in list
for i in range(len(students)):
    students[i] = students[i].split(",")

students.pop()

#number of students who took 0,1,2,...
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]
average = [0,0,0,0,0,0,0,0,0,0,0,0]


for s in students:
    #count is the number of exam taken each students
    count = 0
    #total is the number of total of subject of the students
    total = 0
    for i in range(11):
       if s[i+5]!="-1":
           count += 1
           total += float(s[i+5])

    num_of_exam_taken[count]+=1
    #average is the sum of average of each students
    average[count] += total/count

for i in range(12):
    if num_of_exam_taken[i] != 0:
        average[i] = round(average[i]/num_of_exam_taken[i],2)
        

#plot barchart
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)


figure, axis = plt.subplots()

#plot the barchart using 2 list, high of the bar
plt.bar(x, average)
#change horizontal category name
# plt.xticks(x, x)
#set limit to vertical axis
axis.set_ylim(0,10)

plt.ylabel("Average Point")
plt.title('Average point each students')

# Draw number of students on top of each bar
# label is the number upper the bar
rects = axis.patches
label = average
for rect, label in zip(rects, label):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label,
            ha='center', va='bottom')

plt.show()









