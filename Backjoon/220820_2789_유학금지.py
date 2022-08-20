a = 'CAMBRIDGE'     # 소거해야할 문자를 선언.
word = list(input())    # 입력되는 단어를 리스트 화.

for i in a:             # 선언된 문자를 돌면서.
    for j in range(len(word)):  # 입력된 단어의 스펠링 수만큼 돌면서.
        if i == word[j]:        # 선언된 문자 = 입력된 단어의 인덱스
            word[j] = ''        # 입력된 단어의 인덱스는 공백.
for i in word:                  # 입력된 단어 돌면서.
    print(i, end = '')          # 공백 처리된 단어를 출력.
    