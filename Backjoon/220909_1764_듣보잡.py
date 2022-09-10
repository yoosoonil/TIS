# 참고 : https://wook-2124.tistory.com/476
# 교집합 이용

n, m= map(int, input().split())
# 공백으로 숫자 2개 받음.

a = set()
# set 순서없이 값을 받는데 중복된 값은 쳐낸다.
for i in range(n):
    a.add(input())
# 집합자료형인 set은 add로 값을 추가한다.
# 리스트형인 list는 append로 값을 추가한다.
    
b = set()
for i in range(m):
    b.add(input())
    
result = sorted(list(a & b))
# & 연산자로 a집합자료와 b집합자료를 교집합한다.
# result = ['baesangwook', 'ohhenrie']

print(len(result))

# 리스트를 줄바꿔서 출력하는 법이 2가지있음.
# 1. 리스트를 *(unpacking) 해준 후, sep = "\n"으로 줄바꿔줌.
print(*result, sep = "\n")
# 2. for문으로 하나 씩 뽑아내서 출력.
for i in result:
    print(i)
      

