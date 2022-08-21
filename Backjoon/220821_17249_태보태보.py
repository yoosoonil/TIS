a = input()     # 입력값

i = 0
r = [0, 0]

for c in a:
    if c == '@':
        r[i] += 1
    elif  c == '(':
        i ^= 1          # ^= 뭐임? 1로 고정한다는 것 같은데 뭐지?
    print(i)
# print(*r)       # '*'은 unpacking임. 리스트를 그냥 출력 하는 것은 '*' 이다. ex) print(*[1,2,3]) -> 1 2 3