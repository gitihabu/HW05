print('Running unit tests')
a, b, c = map(int, input().split())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print('Right')
    else: print('Scalene')
else:print('NotATriangle')


