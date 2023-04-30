# 잃어버린 괄호

expression = input()

answer = None

for parts in expression.split('-'):
    if '+' in parts:
        tmp = 0
        for part in parts.split('+'):
            tmp += int(part)
        if answer is None:
            answer = tmp
        else:
            answer -= tmp
    else:
        if answer is None:
            answer = int(parts)
        else:
            answer -= int(parts)


print(answer)
