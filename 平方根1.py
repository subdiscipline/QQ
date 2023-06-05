def absolution(x,y):
    b=x-y
    if b>=0:
        return b
    else:
        return -b
def num(s):
    n=0.0000000000000000000000000000000001
    a=s/2
    for i in range(100):
        b=s/a
        c=absolution(a, b)
        if c<=n:
            break
        else:
            a=a=(a+b)/2
    print("a={:.2f},b={:.2f},c={:.2f}".format((a),(b),(c)))
    print(f'{c<n}')
      
    
x=num(2)