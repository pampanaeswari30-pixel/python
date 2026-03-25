def is_anagram(s,t):
    return sorted(s)==sorted(t)
s=input('enter first name')
t=input('enter second name')
if is_anagram(s,t):
    print('is anagram')
else:
    print('invalid anagram')