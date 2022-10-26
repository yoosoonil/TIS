# 문제 : https://www.acmicpc.net/problem/9093
import sys

T = int(input())

for _ in range(T):
  str = sys.stdin.readline().rstrip()
  words = list(str.split())
  
  for word in words:
    print(word[::-1], end=' ')
