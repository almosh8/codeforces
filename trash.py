def solve():
    x = scan()
    ones = 0
    ans = 0
    b = []
    while x > 0:
        b.append(x % 2)
        x //= 2
    b.reverse()
    for p, n in enumerate(b):
        if n == 1:
            ones += 1
            if ones == 1:
                ans = pow(2, p)
    if ones < 2:
        ans += pow(2, len(b))
    else:
        ans += 1
    output(ans)