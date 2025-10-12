file = open("raw_data.txt","r")

data = file.readline()
data = data.split("\\n") #split cho de nhin

for i in range(len(data)):
    data[i] = data[i].replace("\\r","")
    data[i] = data[i].replace("\\t","")

file = open("test.txt","w")
for i in range(len(data)):
    file.write(data[i]+"\n")

