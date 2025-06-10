a = input()
if a.isalpha():
    if a.islower():
        print(f"{a}(ASCII: {ord(a)}) => {a.upper()}(ASCII: {ord(a.upper())})")
    else:
        print(f"{a}(ASCII: {ord(a)}) => {a.upper()}(ASCII: {ord(a.lower())})")