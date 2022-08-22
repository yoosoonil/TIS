# 참고 : https://jinho-study.tistory.com/680
T = int(input())

for tc in range(1, T + 1):
    n, data = input().split()   # 4 MISSPELL
    n = int(n)  
    print(data[:n-1], data[n:], sep = '')
    # data[:3] = MIS       data[4:] = PELL
    # 처음부터 3미만까지        4초과부터 끝까지
    # pritn => MISPELL
    
# list화해서 없애려고 했는데 슬라이싱하여 단어+단어를 할 줄 몰랐다.
# 코드는 간단하다.