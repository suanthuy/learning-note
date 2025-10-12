s = "<title>Sogiaoduc</title>"
tags = []
for i in range(len(s)):
    if s[i]=="<":
        begin=i
    if s[i]==">":
        end=i
        tags.append(s[begin:end+1])

for tag in tags:
    s = s.replace(tag,"")

print(s)