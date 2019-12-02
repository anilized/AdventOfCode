p = [int(x) for x in open('input2.txt').read().split(',')]
p[1] = 12
p[2] = 2
ip = 0

while True:
    opcode = p[ip]
    print(p[ip])
    i1, i2, i3 = p[ip+1], p[ip+2], p[ip+3]
    if opcode == 1:
        p[i3] = p[i1] + p[i2]
    elif opcode == 2:
        p[i3] = p[i1] * p[i2]
    else:
        assert opcode == 99
        break
    ip += 4

print(p)

