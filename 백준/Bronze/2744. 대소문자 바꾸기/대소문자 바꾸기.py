w = input()
s = ""
for i in w:
    if i.isupper():
        s+=i.lower()
    else:
        s+=i.upper()
print(s)