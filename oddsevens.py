import random
import common

def main():
    even = 0
    odd = 0
    pad = 3
    max_iter = 1 * 10**(pad-1)
    message = []

    for i in range(max_iter):
        d = random.choice(common.die20)
        if d % 2 == 0:
            even += 1
            message.append(f"{i+1:{pad}}) {d} even")
        else:
            odd += 1
            message.append(f"{i+1:{pad}}) {d} odd")
    #end for
    
    for m in message:
        print(m)
    #end for

    print("\n\nEven/Odd Test results")
    print(f"Even:  {even}")
    print(f"Odd:   {odd}")
    print(f"Even:  {even/max_iter:.2%}")
    print(f"Odd:   {odd/max_iter:.2%}")
    
#end main

if __name__ == "__main__":
    main()