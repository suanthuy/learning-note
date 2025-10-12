file = open("raw_data.txt","r")

data = file.readline()

#make data become a list
data = data.split("\\n")  #split the data to many lines

#remove /r and /t
for i in range(len(data)):
    data[i] = data[i].replace("\\r","")
    data[i] = data[i].replace("\\t","")

for i in range(len(data)):
    tags=[]
    #data[i] is a str of a line
    for j in range(len(data[i])):  #check the word of line is < or >
        if data[i][j] =="<":        #attention not begin=i, begin=j
            begin=j
        if data[i][j] ==">":
            end=j
            tags.append(data[i][begin:end+1])
    #remove tag
    for tag in tags:
        data[i] = data[i].replace(tag,"")

#write to the new file
file = open("Unit2.5_file.txt","w")
for i in range(len(data)):
    file.write(data[i]+"\n")





