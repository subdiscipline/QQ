import random

n = 1000000  
count = 0 

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        count += 1

pi = 4 * count / n  
print(f"圆周率的估计值为：{pi:.2f}")