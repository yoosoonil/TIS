# 참고 : https://minwin.tistory.com/30

import sys

pe = {}

for _ in range(int(sys.stdin.readline())):
    p, c = sys.stdin.readline().rstrip().split()
            # rstrip : string의 오른쪽에서 제거
            # lstrip : string의 왼쪽에서 제거
            # strip : 왼쪽과 오른쪽에서 제거(양쪽에서 제거)
            # p(people), c(counter) : Baha enter
    
    if c == 'enter':
        pe[p] = 'enter'
    else :
        if pe[p]:
            del pe[p]
for people in sorted(pe, reverse = True):
    print(people)
    