# 문제풀이참고 : https://assaeunji.github.io/python/2020-05-06-bj1302/
# list comprehension 참고 : https://dojang.io/mod/page/view.php?id=2285

N = int(input())    # 입력 개수 N을 받는다.

book_list = []      # book_list와 unique_list를 빈 리스트로 초기화.
unique_list = []

for i in range(1, N + 1):
    book_list.append(input())   # book_list에 N번만큼 책이름 추가.
    
for x in book_list:             # book_list에서 책이름을 꺼낸다.
    if x not in unique_list:    # unique_list에 책이름이 없다면
        unique_list.append(x)   # unique_list에추가.
        # 결국, 책이름이 한번씩 unique_list에 저장됨.
        
count = [book_list.count(x) for x in unique_list]
# list comprehension 활용
# # unique_list에서 하나씩 나오쥬? -> [top, kimtop]
# book_list.count(top), book_list.count(kimtop)
# count = [4, 1]
idx = []

for i in range(len(count)):
    if count[i]==max(count):
        idx.append(i)
    # idx = [0]


print(sorted([unique_list[i] for i in idx])[0])
    # i =0 -> unique_list[0] -> top 
    # 정렬된 값 중 [0](첫번째) 값을 출력.
    # 어차피 한개임.
    
    