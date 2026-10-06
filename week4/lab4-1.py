def CarryDetection(a, b):
    count = 0
    carry = 0
    b = b.zfill(len(a))

    for i in range(len(a) - 1, -1, -1):
        if((int(a[i]) + int(b[i]) + carry) >= 10):
            count += 1
            carry = 1
        else:
            carry = 0

    return count


while(True):
    a, b = input().split()

    if(a == "0" and b == "0"):
        break

    if(len(a) >= len(b)):
        count = CarryDetection(a, b)
    else:
        count = CarryDetection(b, a)

    if(count == 0):
        print("No carry operation.")
    elif(count == 1):
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")