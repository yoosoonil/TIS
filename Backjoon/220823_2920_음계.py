# 참고 : https://wook-2124.tistory.com/469

num = list(map(int, input().split()))

if num == sorted(num):
    print('ascending')
elif num == sorted(num, reverse = True):
    # reverse = True 걸어서 역순(내림차순)정렬.    
    print('descending')
else:
    print('mixed')