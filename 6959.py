T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int,list(input())))
    cnt = 0
    while len(num) > 1:
        #print(num)
        cnt += 1
        a = num.pop(0)
        b = num.pop(0)
        num.append((a+b)%10)
        if a+b> 9:
            num.append(1)
    if cnt %2 == 1:
        res = "A"
    else:
        res = "B"
    print("#" + str(test_case) + " " + res)
