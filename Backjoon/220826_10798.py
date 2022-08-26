# 5줄을 입력받고, 최대 길이 15의 문자열 입력
# 참고 : https://www.acmicpc.net/problem/10798

words = []
length = []

for i in range(5):
    word = input()
    words.append(word) # 입력된 값을 words에 리스트화
    length.append(len(word)) # 입력된 값의 가로줄의 길이를 리스트화
rst = ''

for i in range(max(length)):    
    # 가로줄의 최대값 가지고와서 최대까지 읽어나감.
    for j in range(5):
        # 세로는 5로 고정값.
        if i < length[j]:
            rst += words[j][i]

print(rst)
