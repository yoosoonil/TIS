# stdin.readlines 참고 : https://xsop.tistory.com/40
import sys

x =  []
# 숫자들 담아둘 x 리스트

for i in range(10):
    x.append(int(input()))
    # x리스트에 input 숫자 추가.
print(int(sum(x) / 10))
    # 리스트에 있는 것들 더하고 10으로 나눠서 평균값 구함.

y = list(set(x))
print(y)
# 리스트에 있는거에서 중복값들 제거(set함수 활용)
z = []
# 빈출값 도출 z리스트
for i in range(len(y)):
    z.append(x.count(y[i]))
    # y리스트에 있는 것들이 x에 있다면 그것의 중복값 확인
    # z리스트에 카운트값 추가

print(z)

# print(y[z.index(max(z))])
    # z리스트 중에 max값에 해당하는 것
    # z.index(3) 3이라는 문자 위치 찾기 -> 6
    # y[6] = 30

  