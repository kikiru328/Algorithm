T = input()
print(f"LETTERS {len([w for w in T if w.isalpha()==True])}")
print(f"DIGITS {len([d for d in T if d.isdigit()==True])}")