s="Hello World"
print("String:",s)
#len(): length of the string 
print("Length:",len(s))
#index s[0],s[1],... 
print("Index:",s[0],s[1],s[2])
print("-------------")
for i in range(len(s)):
    print(s[i])
#index -1 
print("-------------")
print("Index -1:",s[-1])
print("Index -2:",s[-2])
#split ---> result is a list
print("-------------")
print("Split string s:",s.split(" "))
#replace
print("-------------")
print("Replace l-->x:",s.replace("l","x"))
#slice s[0:1]=s[0]
print("-------------")
print("s[0:3]:",s[0:3])
print("s[5:]:",s[5:])
print("s[0:-1]:",s[0:-1]) #print string s from index 0 to and not equal the last
#upper()
print("-------------")
print("s[0].upper:",s[0].upper())
a = s.upper()
print("s.upper:",a)
#lower()
print("-------------")
print("s.lower:",s.lower())
print("a.lower:",a.lower())
#islower(), isupper()
#title ---> uppercase the first letter of any words
print("-------------")
b = s.lower()
print("String b:",b)
print("b.title:",b.title())
#swapcase
print("-------------")
print("s.swapcase:",s.swapcase())
#strip ---> delete the whitespace character
print("-------------")
t = "    Hello World    "
print("String t:",t)
print("t.strip:",t.strip())
print("t.lstrip:",t.lstrip())
print("t.rstrip:",t.rstrip())
#isdigit()---> check co la chu so hay ko
#find --> find the index of the character of the string
print("-------------")
print("Find 'l':",s.find("l"))
print("Find 'o':",s.find('o'))
###Example
print("-------------")
world_position=s.find("World")
s1=s[:world_position]
s2="Super "
s3=s[world_position:]
s4=s1+s2+s3
print("s4 =",s4)
#count
print("-------------")
print("count 'l':",s.count("l"))








