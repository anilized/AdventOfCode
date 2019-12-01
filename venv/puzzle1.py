import math


def q1():
    total = 0
    with open("input.txt") as file:
        for line in file:
            total += math.floor(int(line) / 3) - 2

    print(total)


q1()


def q2():
    total = 0
    with open('input.txt') as file:
        for line in file:
            next_fuel = int(line)
            fuel_tot = 0
            while True:
                next_fuel = math.floor(next_fuel / 3) - 2

                if next_fuel > 0:
                    fuel_tot += next_fuel
                else:
                    break
            total += fuel_tot
    print(total)


q2()
