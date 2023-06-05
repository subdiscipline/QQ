def absolution(x,y):
    b=x-y
    if b>=0:
        return b
    else:
        return -b

def num(s):
    n=0.0000000000000000000000000000000001
    a=s/2
    while True:
        b=s/a
        c=absolution(a, b)
        print("a={:.2f},b={:.2f},c={:.2f}".format((a),(b),(c)))
        print(f'{c<=n}')
        if c<=n:
            break
        else:
            a=a=(a+b)/2
    
x=num(100)
