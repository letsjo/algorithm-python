# 크로아티아 알파벳

croatiaLetter = ['dz=', 'z=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=']

croatiaWord = input()

for letter in croatiaLetter:
    croatiaWord = croatiaWord.replace(letter, '_')

print(len(croatiaWord))
