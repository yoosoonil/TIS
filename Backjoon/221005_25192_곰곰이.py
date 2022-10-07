# 참고 : https://lbdiaryl.tistory.com/334

N = int(input())

dic = {}  # dic 정의

cnt = 0  # cnt는 0으로 초기화

for _ in range(N):
    Input = input()  # input 정의

    if Input == "ENTER":  # input에 'ENTER' 입력된다면,
        for key, value in dic.items():  # 딕셔너리의 key, value를 가져옴. 이거 moviereview 프로젝트에 쓰임.
            if value == 1:  # value가 1이라면,
                cnt += 1  # cnt에 1추가.
        dic = {}

    else:  # 'ENTER'가 Input값이 아니라면 아래 진행.
        if Input not in dic:  # 딕셔너리에 input 값이 없다면,
            dic[Input] = 1  # 딕셔너리의 input값에 해당하는 key의 value는 1로 설정.


for key, value in dic.items():  # 딕셔너리의 key, value값 불러옴.
    if value == 1:  # value값이 1이라면,
        cnt += 1  # cnt 값에 추가.
        # {'pjshwa': 1, 'chansol': 1, 'chogahui05': 1, 'lms0806': 1, 'pichulia': 1, 'r4pidstart': 1, 'swoon': 1, 'tony9402': 1}

print(cnt)  # 결국, 8이 나옴.
