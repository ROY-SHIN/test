num=[]
etc=[]
for a in range(0, 6):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0,10):
                num.append(1001*a+101*b+11*c+2*d)
                etc.append(1000*a+100*b+10*c+d)

self_number = set(etc)-set(num)
print(sum(self_number))
