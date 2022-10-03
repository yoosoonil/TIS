# 문제를 파악해보자.
# 노트 2에 들어간 숫자가 노트 1에 들어간 숫자들에 있다면,
# 그 숫자는 1로 출력하고, 없으면 0을 출력한다.

import sys

input = sys.stdin.readline

t = int(input())  # 테스트개수임.

for _ in range(t):  # 1이기 때문에 for문 한번만 돌릴거임.
    n = int(input())  # 5 들어갈거임.
    note1 = set(
        sys.stdin.readline().split()
    )  # 주어진 4 1 5 2 3이 한칸 씩 띄우면서 들어감. set으로 중복되는 건 지울거임.
    M = int(input())
    note2 = list(
        sys.stdin.readline().split()
    )  # 1 3 7 9 5가 들어갈거임. list 함. [1, 3, 7, 9, 5]
    for i in note2:  # note2의 리스트에서 하나씩 꺼낼거임.
        if i in note1:  # note1에서 하나씩 꺼내는 것이 note2의 것과 일치한다면 1을 프린트
            print(1)
        else:  # 그게 아니라면 0 프린트
            print(0)
