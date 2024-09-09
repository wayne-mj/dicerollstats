import random
die6 = [1, 2, 3, 4, 5, 6]
die10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
die20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def main():
    even = 0
    odd = 0
    pad = 3
    max_iter = 1 * 10**(pad-1)
    message = []

    for i in range(max_iter):
        d = random.choice(die20)
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