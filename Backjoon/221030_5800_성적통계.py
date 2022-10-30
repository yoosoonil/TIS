n = int(input())

s = []

for j in range(1, n+1):
  s = list(map(int, input().split()))
  s = s[1:]
  list_s = sorted(s)
  lg = 0
  
  for i in range(0, len(list_s)-1):
    # 계속 앞의 lg와 비교하면서 점수차가 큰 것을 찾는 것
    if list_s[i+1] - list_s[i] > lg :
      lg = list_s[i+1] - list_s[i]
  print(f'Class {j}')
  print(f'Max {max(list_s)}, Min {min(list_s)}, Largest gap {lg}')
  