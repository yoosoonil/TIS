# 5,6을 잘못본다고함. 5가 6으로 6이 5로 바뀜.
# 5 or 6이 1의자리, 10의자리, 100의자리, 1000의자리에 따라
# 그만큼 값이 차이나고, 그만큼 합에서 차이가 남.

# 하지만, 최소값과 최대값을 구하는 것이기에
# replace method로 풀 수 있음.

a, b = input().split()

min_num = int(a.replace('6', '5')) + int(b.replace('6','5'))
max_num = int(a.replace('5', '6')) + int(b.replace('5','6'))

print(min_num, max_num) 