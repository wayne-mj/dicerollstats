import random
import common

# Can n be a square root?
def can_sqrt(n):
    return n**0.5 % 1 == 0

# Can n be a square?
def can_sqr(n, die):
    return n**2 <= die[-1]

# Test the functions
def main():
    is_sqrt = 0
    isnot_sqrt = 0
    is_sqr = 0
    isnot_sqr = 0
    pad = 3
    max_iter = 1 * 10**(pad-1)
    chksqrt = True
    message = []

    for i in range(max_iter):
        d = random.choice(common.die20)
        if chksqrt:
            if can_sqrt(d):
                is_sqrt += 1
                message.append(f"{i+1:{pad}}) {d} is a square root")
            else:
                isnot_sqrt += 1
                message.append(f"{i+1:{pad}}) {d} is not a square root")
        else:
            if can_sqr(d, common.die20):
                is_sqr += 1
                message.append(f"{i+1:{pad}}) {d} is a square")
            else:
                isnot_sqr += 1
                message.append(f"{i+1:{pad}}) {d} is not a square")
    #end for
    
    for m in message:
        print(m)
    #end for

    if chksqrt:
        print("\nSquare Root Test results")
        print(f"Square Root:       {is_sqrt}")
        print(f"Not Square Root:   {isnot_sqrt}")
        print(f"Square Root:       {is_sqrt/max_iter:.2%}")
        print(f"Not Square Root:   {isnot_sqrt/max_iter:.2%}")
    else:
        print("\nSquare Test results")
        print(f"Square:       {is_sqr}")
        print(f"Not Square:   {isnot_sqr}")
        print(f"Square:       {is_sqr/max_iter:.2%}")
        print(f"Not Square:   {isnot_sqr/max_iter:.2%}")
#end main

if __name__ == "__main__":
    main()