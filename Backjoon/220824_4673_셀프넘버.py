num = set(range(1, 10001))
num_1 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
        num_1.add(i)
        
self_num = sorted(num - num_1)
for i in self_num:
    print(i)