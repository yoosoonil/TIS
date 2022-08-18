# 참고 : https://wook-2124.tistory.com/222

n = int(input()) # 68

num = n
cycle = 0

while True:
    a = num // 10       # 10으로 나눠서 몫 = 6
    b = num % 10        # 10으로 나눠서 나머지 = 8
    c = (a + b) % 10    # 10으로 나눠서 나머지 = 4
    num = (b * 10) + c  # 84
    
    cycle += 1
    if num == n:        # num이 처음 입력 값 n과 같아지면 break
        break

print(cycle)