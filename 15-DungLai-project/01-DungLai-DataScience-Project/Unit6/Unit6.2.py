#read  file
with open("clean_data.csv",encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

#split header
header = header.split(',')
subject = header[5:]

#split each students in list 
for i in range(len(students)):
    students[i] = students[i].split(",")

#remove the last students
students.pop()

#get number of students per age group
# 17,18,19,...-->>=27
num_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
average_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]

for s in students:
    age = 2020 - int(s[4])
    if age >=27:
        age = 27
    num_of_student_per_age_group[age - 17] += 1

    count_score = 0     #count of subjects each students
    total_score = 0     #sum of scores each students
    for i in range(11):
        if s[i+5] != "-1":
            count_score += 1
            total_score += float(s[i+5])
    average_of_student_per_age_group[age -17] += total_score/count_score

#percentage "average_of_student_per_age_group"
for i in range(len(average_of_student_per_age_group)):
    average_of_student_per_age_group[i] = round(average_of_student_per_age_group[i]/num_of_student_per_age_group[i],2)

#scale "average_of_student_per_age_group" from 0 to 10 became 0 to 70000
for i in range(len(average_of_student_per_age_group)):
    average_of_student_per_age_group[i] = average_of_student_per_age_group[i]*7000


#plot barchart
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = np.arange(11)

age = ["17","18","19","20","21","22","23","24","25","26",">26"]

figure, axis = plt.subplots()

#plot the barchart using 2 list, high of the bar
plt.bar(x, num_of_student_per_age_group)
plt.plot(x,average_of_student_per_age_group, color="r", marker="o")
#change horizontal category name
plt.xticks(x, age)
#set limit to vertical axis
axis.set_ylim(0,70000)

plt.ylabel("Number of students per age group")
plt.xlabel("Age of students")
plt.title("Average point of students per age group")

#right side axis ticks 
ax2 = axis.twinx()
ax2.tick_params("y",colors = "r")
ax2.set_ylabel("Average point",color = "r")
ax2.set_ylim(0,10)

# Draw number of students on top of each bar
# label is the number upper the bar
rects = axis.patches
label = num_of_student_per_age_group
for rect, label in zip(rects, label):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label, ha='center', va='bottom')

plt.show()



