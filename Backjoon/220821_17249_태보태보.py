a = input()     # 입력값

i = 0
r = [0, 0]

for c in a:
    if c == '@':
        r[i] += 1
    elif  c == '(':
        i ^= 1        # ^= XOR 연산자임. XOR 연산자를 공부하도록.
print(*r)       # '*'은 unpacking임. 리스트를 그냥 출력 하는 것은 '*' 이다. ex) print(*[1,2,3]) -> 1 2 3