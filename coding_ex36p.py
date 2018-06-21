num=[]
etc=[]
for a in range(0, 10):
    for b in range(0, 10):
        num.append(11*a+2*b)
        etc.append(10*a+b)

self_number = set(etc)-set(num)
print(sum(self_number))
