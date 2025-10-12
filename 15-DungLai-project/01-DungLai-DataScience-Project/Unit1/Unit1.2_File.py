"""
"Open" command uses to read, write, append the file.
open("name of the file", "a letter")
r: read
w: write
a: appending to the end of file
b: binary mode
+: updating (reading and writing) 
"""

file = open("data.txt","w")

for i in range(5):
    file.write("Number: "+str(i)+"\n")


file = open("data.txt","a")

for i in range(5,10):
    file.write("Number: "+str(i)+"\n")

file = open("data.txt","r")
line = file.read().split("\n")
for i in range(len(line)):
    print("line "+str(i+1)+": "+line[i])
print(len(line)) ##11


