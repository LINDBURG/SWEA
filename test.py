import copy
#import sys
#sys.stdin = open("input.txt", "r")


def check(board, maxinos, c_num, l_num, answer, s):
    if c_num + len(maxinos) < answer[0]:
        return 0
    if maxinos:
        chip = maxinos[0]
        maxinos = maxinos[1:]
    else:
        #print(s)
        #for b in board:
            #print(b)
        #print(s)
        if answer[0] < c_num or (answer[0] <= c_num and answer[1] > l_num):
            #print(answer, c_num, l_num)
            answer[0] = c_num
            answer[1] = l_num
        return 0
    
    if chip[0] == 0 or chip[0] == len(board)-1 or chip[1] == 0 or chip[1] == len(board)-1:
        #print("side")
        check(board, maxinos, c_num+1, l_num, answer, s+"S")
    else:
        # 1 1   7 7 왼쪽
        #print("L")
        n_board = copy.deepcopy(board)
        cnt = -1
        for i in range(chip[0]-1,-1,-1):
            if cnt == -1:
                cnt += 1
            if n_board[i][chip[1]] == 1:
                cnt = -1
                break
            n_board[i][chip[1]] = 1
            cnt += 1
        #print(cnt)
        if cnt != -1:
            check(n_board,maxinos, c_num + 1, l_num + cnt, answer, s+"L")
            
        # 1 1   7 7 오른쪽
        #print("R")
        n_board = copy.deepcopy(board)
        cnt = -1
        for i in range(chip[0]+1,len(board)):
            if cnt == -1:
                cnt += 1
            if n_board[i][chip[1]] == 1:
                cnt = -1
                break
            n_board[i][chip[1]] = 1
            cnt += 1
        #print(cnt)
        if cnt != -1:
            check(n_board,maxinos, c_num + 1, l_num + cnt, answer, s+"R")
            
        # 1 1   7 7 위쪽
        #print("U")
        n_board = copy.deepcopy(board)
        cnt = -1
        for j in range(chip[1]-1,-1,-1):
            if cnt == -1:
                cnt += 1
            if n_board[chip[0]][j] == 1:
                cnt = -1
                break
            n_board[chip[0]][j] = 1
            cnt += 1
        #print(cnt)
        if cnt != -1:
            check(n_board,maxinos, c_num + 1, l_num + cnt, answer, s+"U")
            
        # 1 1   7 7 아래쪽
        #print("D")
        n_board = copy.deepcopy(board)
        cnt = -1
        for j in range(chip[1]+1,len(board)):
            if cnt == -1:
                cnt += 1
            if n_board[chip[0]][j] == 1:
                cnt = -1
                break
            n_board[chip[0]][j] = 1
            cnt += 1
        #print(cnt)
        if cnt != -1:
            check(n_board,maxinos, c_num + 1, l_num + cnt, answer, s+"D")
            
        # 1 1   7 7 패스
        #print("P")
        n_board = copy.deepcopy(board)
        check(n_board,maxinos, c_num, l_num, answer, s+"P")
            

T = int(input())

for test_case in range(T):
    board = []
    maxinos = []
    answer = [0,0]
    N = int(input())
    for i in range(N):
        board.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                maxinos.append([i,j])
    #print(maxinos)
    check(board, maxinos, 0, 0, answer, "")
    #print(answer)
    print("#" + str(test_case+1) +" " + str(answer[1]))
    
