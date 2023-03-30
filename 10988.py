# 팰린드롬인지 확인하기

word = input()

if (word == ('').join(word[::-1])):
    print(1)
else:
    print(0)
