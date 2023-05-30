# 단어 뒤집기 2
import sys
input = sys.stdin.readline

sentence = list(input().strip())
word_stack = ''
answer = ''
reverse = True;

for letter in sentence:
    if letter == ' ':
        answer += word_stack+' '
        word_stack = ''
        continue
    elif letter == '<':
        answer += word_stack+'<'
        word_stack = ''
        reverse = False
        continue
    elif letter == '>':
        answer += word_stack+'>'
        word_stack = ''
        reverse = True
        continue

    if (reverse):
        word_stack = letter + word_stack
    else:
        word_stack += letter

answer += word_stack
print(answer)