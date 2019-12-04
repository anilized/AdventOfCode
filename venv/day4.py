# part 2 cuz part 1 is easy

c = 0
for i in range(402328, 864247 + 1):
    inc, doub = True, False
    d_old = None
    while i > 0:
        d = i % 10
        i = i // 10
        d_ = i % 10
        # Not increasing:
        if d_ > d:
            inc = False
            break
        # Double, but not with the same digit before or after:
        if d_ == d and not ((i // 10) % 10 == d or d == d_old):
            doub = True
        d_old = d

    if not (inc and (doub == 1)): continue
    c += 1
print(c)
