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


#remove empty line
unempty_lines=[]
for i in range(len(data)):
    if data[i]!="":
        unempty_lines.append(data[i])
data = unempty_lines

#name, dob, score
name = data[7]
dob = data[8]
score = data[9]

#load unicode table
chars = []
codes = []

file = open("unicode.txt",encoding="utf8")
unicode_table = file.read().split("\n")
for code in unicode_table:
    x = code.split(" ")
    chars.append(x[0])
    codes.append(x[1])

#replace code by char
for i in range(len(codes)):
    name =  name.replace(codes[i],chars[i])
    score = score.replace(codes[i],chars[i])

#replace &# in name and score
for i in range(len(name)):
    if name[i:i+2] == "&#":
        name = name[:i]+ chr(int(name[i+2:i+5]))+name[i+6:]
for i in range(len(score)):
    if score[i:i+2] == "&#":
        score = score[:i]+ chr(int(score[i+2:i+5]))+score[i+6:]

data = [name, dob, score]

#write to the new file
file = open("Unit2.9_Unicode.txt",encoding="utf8",mode="w")
for i in range(len(data)):
    file.write(data[i]+"\n")



