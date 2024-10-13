import random
import common

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    yes_prime = 0
    no_prime = 0
    pad = 4
    max_iter = 1 * 10**(pad-1)
    message = []

    for i in range(max_iter):
        d = random.choice(common.die20)
        if prime(d):
            yes_prime += 1
            message.append(f"{i+1:{pad}}) {d} Prime")
        else:
            no_prime += 1
            message.append(f"{i+1:{pad}}) {d} Not Prime")
    #end for
    
    for m in message:
        print(m)
    #end for

    print("\n\nPrime Number Test results")
    print(f"Prime:      {yes_prime}")
    print(f"Not Prime:  {no_prime}")
    print(f"Prime       {yes_prime/max_iter:.2%}")
    print(f"Not Prime   {no_prime/max_iter:.2%}")
    
#end main

if __name__ == "__main__":
    main()