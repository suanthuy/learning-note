#read file
with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_students = len(students)

#split header
header = header.split(",")
subject = header[5:]
#split each student in list
for i in range(len(students)):
    students[i] = students[i].split(",")

#remove the last student (empty student)
students.pop()

name = [] #list of last name
name_count = []  #list of the number of lastnames #danh sach so hoc sinh cung ho

for s in students:
    s_name = s[1].split(" ") #ten cua hoc sinh s
    lastname = s_name[0]
    if lastname not in name:
        name.append(lastname)
        name_count.append(0)
        name_count[name.index(lastname)] += 1
    else:
        name_count[name.index(lastname)] += 1

sort_index = []
counted_max_num = []
# tao counted_max_num, danh sach so lan lap cac ho lon nhat
for i in range(len(name)):
    max_number = 0
    for j in range(len(name)):
        if name_count[j] > max_number and name_count[j] not in counted_max_num:
            max_number = name_count[j]

    counted_max_num.append(max_number)

# print(sum(name_count))
# print(counted_max_num)

# tao sort_index, vi tri number from high to low with counted_max_num
for max_num in counted_max_num:
    for i in range(len(name)):
        if name_count[i] == max_num and i not in sort_index:
            sort_index.append(i)

# print(sort_index)
# print(len(sort_index))

name_sorted = []            #danh sach ho da sap xep
name_count_sorted = []      #danh sach so lan lap ho da sap xep
#use sort_index to sort name and name_count
for index in sort_index:
    name_count_sorted.append(name_count[index])
    name_sorted.append(name[index])

print(name_count_sorted)
print(name_sorted)
# draw barchart











