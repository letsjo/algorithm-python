# 단어 공부

word = input().upper()
dict_letter = {}

for letter in word:
    if letter not in dict_letter:
        dict_letter[letter] = 1
    else:
        dict_letter[letter] += 1

# 최대값을 뽑아주지만, 제일 앞 쪽에 있는 하나만 뽑아준다.
# print(max(dict_letter, key=dict_letter.get))

# 여러개를 체크하려면, 리스트 컴프리핸션을 써야한다.
result = [k for k, v in dict_letter.items() if max(dict_letter.values()) == v]

if len(result) > 1:
    print('?')
else:
    print(result[0])
