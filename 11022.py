# A+B - 8

T = int(input())

for i in range(T):
    input_data = input().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(f'Case #{i+1}: {A} + {B} = {A+B}')
