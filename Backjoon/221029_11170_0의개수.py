T = int(input())

for _ in range(T):
  n, m = map(int, input().split())
  cnt = 0
  for i in range(n, m+1):
    str_i = str(i)
    # 문자열에서 '0'이 포함된 숫자를 찾으려니
    # 숫자를 문자로 바꿔주는 str메서드 사용
    cnt += str_i.count('0')

  print(cnt)
# cnt를 첫 for문위로 빼는것과 안쪽으로 넣는 것.
# 답이 다름. 이유를 알아보자.