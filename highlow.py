import random
import common

def main():
    high = 0
    low = 0
    pad = 5
    max_iter = 1 * 10**(pad-1)
    message = []
    test_point = 3  # Low/High mark for die sets 3 for 1-6, 5 for 1-10, and 10 for 1-20

    for i in range(max_iter):
        d = random.choice(common.die6)
        if d > test_point:
            high += 1
            message.append(f"{i+1:{pad}}) {d} high")
        else:
            low += 1
            message.append(f"{i+1:{pad}}) {d} low")
    #end for
    
    for m in message:
        print(m)
    #end for

    print("\n\nHigh/Low Test results")
    print(f"High: {high}")
    print(f"Low:  {low}")
    print(f"High  {high/max_iter:.2%}")
    print(f"Low   {low/max_iter:.2%}")
    
#end main

if __name__ == "__main__":
    main()