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
    #remove whitespace from list
    data[i] = data[i].strip()
"""
# remove empty line
# if do like the code blow --> error: line 31, list index out of range              
# for i in range(len(data)):
#     if data[i] == "":
#         data.remove(data[i])
"""
#remove empty line
unempty_lines=[]
for i in range(len(data)):
    if data[i]!="":
        unempty_lines.append(data[i])
data = unempty_lines

#write to the new file
file = open("Unit2.6_DeleteSpace.txt","w")
for i in range(len(data)):
    file.write(data[i]+"\n")