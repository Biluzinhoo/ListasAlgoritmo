import random
num = []
while len(num)<6:
    n=random.choice(range(1, 61))
    if n not in num:
        num.append(n)
    
num.sort()
for x in num:
    print(x)