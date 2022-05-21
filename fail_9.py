x = 1000


def pythag(a, b,):
    c = (a**2 + b**2)**(0.5)
    return c


def pythag_trip(a, b):
    if a < b < pythag(a, b) and a + b + pythag(a, b) == 1000:
        # print(a*b*(pythag(a,b)))
        return True
    return False


if pythag_trip(200,375):
    print("hello")
else:
    print("no")
"""
a = 200
b = 375

if pythag_trip(a, b):
    print(a*b*pythag(a, b))
elif a == b:
    a = 1
    b += 1
else:
    a += 1
"""
for a in range(1,200):
    b = 1
    if pythag_trip(a,b):
        print(a*b*(pythag(a,b))):
    elif a == b:
        a = 1
        b += 1


