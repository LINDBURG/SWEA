T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    link = [[i+1] for i in range(N)]
    
    for m in range(M):
        a, b = map(int, input().split())
        idx_a, idx_b = -1,-1
        for i in range(len(link)):
            if a in link[i]:
                idx_a = i
            if b in link[i]:
                idx_b = i
        
        if idx_a == idx_b:
            continue
        link[idx_a].extend(link[idx_b])
        link.pop(idx_b)
    print("#" + str(test_case) + " " + str(len(link)))
