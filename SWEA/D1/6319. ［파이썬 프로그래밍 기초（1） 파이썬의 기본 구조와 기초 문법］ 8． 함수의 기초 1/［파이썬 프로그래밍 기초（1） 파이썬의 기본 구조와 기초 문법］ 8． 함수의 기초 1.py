t = input()
def palindrome(t):
    p = ""
    for i in t[::-1]:
        p += i
    if t == p:
        print(t)
        print("입력하신 단어는 회문(Palindrome)입니다.")
        
palindrome(t)