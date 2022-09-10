# 문제풀이 참고 : https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-11652-%EC%B9%B4%EB%93%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# 딕셔너리 참고 : https://hun931018.tistory.com/56
# sorted lambda 참고 : https://gorokke.tistory.com/38

# B = {}
# for i in range (5):
#     B[i] = i
# print(B)
# -> {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

# numbers = [1,2,6,8,4,3,2,1,9,5]
# counter ={}
# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1
#     print(counter)


import sys
input = sys.stdin.readline

n = int(input())
card_dic = {}
# 이 문제는 for문으로 돌리면 시간초과 남
# 딕셔너리 사용해서 풀어야함.

for i in range(n):
    card = int(input())     # card 숫자 들어간다
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1
# {1: 1}
# {1: 1, 2: 1}
# {1: 2, 2: 1}
# {1: 2, 2: 2}
# {1: 3, 2: 2}

result = sorted(card_dic.items(), key = lambda x : (x[0],-x[1]))
# card_dic.items() : card_dic라는 딕셔너리에서 key/value 모두 출력
# 정렬 하겠다는건데, -를 붙이면, 현재와 반대차순으로 정렬
# -x[1],x[0] -> x[1] 값을 내림차순하고, x[1]값이 같다면 x[0]은 오름차순
# [(1, 3), (2, 2)]
 
print(result[0][0])
# result의 두개 묶인 것에서 첫인덱스의 첫인덱스를 프린트함.