T = int(input())

for test_case in range(1, T + 1):
    names = []
    N = int(input())
    for i in range(N):
        names.append(input())
    names = sorted(list(set(names)), key=lambda x:(len(x),x))
    print("#" + str(test_case))
    for name in names:
        print(name)
