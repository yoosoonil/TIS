# 참고 : https://velog.io/@cosmos/BOJ%EB%B0%B1%EC%A4%80-11945-python

# 주어진 list를 좌우로 뒤집어지게 해야함

def solve(l: list) -> str:
  return '\n'.join([x[0][::-1] for x in l])

if __name__ == '__main__':
  n, m = map(int, input().split()) # x축, y축 입력
  if m == 0:  # y축이 0이라면 값이 없는 것이니 공백 프린트
    print()
  else:
    bbang = [list(map(str, input().split())) for _ in range(n)]
    print(bbang)
    print(solve(bbang)) 