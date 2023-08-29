def febinoicci(n):
    a = 0
    b = 1
    for i in range(n):
        a,b=b,a+b
        yield a


k=febinoicci(10)
print(k)
for i in k:
    print(i)