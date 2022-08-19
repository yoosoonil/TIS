N = int(input())

list_ = list(map(int, input().split()))

print(min(list_), max(list_), end = ' ')

# 풀이 시간이 408 ms가 나오므로, 다른 풀이 참고함.
# 참고 : https://yaneodoo2.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-10818%EB%B2%88-%EC%B5%9C%EC%86%8C-%EC%B5%9C%EB%8C%80-%EC%B5%9C%EC%86%9F%EA%B0%92%EA%B3%BC-%EC%B5%9C%EB%8C%93%EA%B0%92%EC%9D%84-%EC%B0%BE%EB%8A%94-%EB%AC%B8%EC%A0%9C

N = int(input())

list_ = list(map(int, input().split()))

list_.sort()
print(list_[0], list_[-1])

