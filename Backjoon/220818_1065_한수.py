# 어떤 양의 정수 x 각 자리가 등차 수열을 이룬다면, 그 수를 한수라 한다.

num = int(input())

hansu = 0
for i in range(1, num + 1):
    num_list = list(map(int, str(i)))
    print(num_list)
    if i < 100:
        hansu += 1 # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1 # num의 각 자리가 등차 수열이면 한수
print(hansu)

# 110 입력하면 99가 출력.
# why? 1~110까지 하나씩 싹 다 호출.
# 1~9 -> 한자리수들은 모두가 한수.
# 10~99 -> 각자가 등차가 한개이기에 모두 한수.
# 100~110 -> 등차가 되는 것이 없음. 모두 다 한수 x.
# 따라서 한수의 개수는 99개.