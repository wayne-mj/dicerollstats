import random
die6 = [1, 2, 3, 4, 5, 6]
die10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
die20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def main():
    high = 0
    low = 0
    pad = 5
    max_iter = 1 * 10**(pad-1)
    message = []
    test_point = 3  # Low/High mark for die sets 3 for 1-6, 5 for 1-10, and 10 for 1-20

    for i in range(max_iter):
        d = random.choice(die6)
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