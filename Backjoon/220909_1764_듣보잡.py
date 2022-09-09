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

print(*result, sep = "\n")
# for i in result:
#     print(i)
      

