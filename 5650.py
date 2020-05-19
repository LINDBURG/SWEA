

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = []
    score = 0
    worm = [[] for i in range(5)]
    for i in range(N):
        line =list(map(int,input().split()))
        board.append(line)
        for j in range(N):
            if line[j] >5:
                worm[line[j]-6].append([i,j])
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for direction in range(4):
                    cnt = 0
                    nx, ny, nd = i,j,direction
                    while True:
                        #다음 블럭이 무엇인지 확인
                        if nd == 0 and ny < len(board) -1 and board[nx][ny+1] != 5 and board[nx][ny+1] != 1 and board[nx][ny+1] != 2 :
                            ny += 1
                            if board[nx][ny] == 3:
                                nd = 1
                                cnt += 1
                            elif board[nx][ny] == 4:
                                nd = 3
                                cnt += 1
                        elif nd == 1 and nx < len(board) -1 and board[nx+1][ny] != 5 and board[nx+1][ny] != 2 and board[nx+1][ny] != 3:
                            nx += 1
                            if board[nx][ny] == 1:
                                nd = 0
                                cnt += 1
                            elif board[nx][ny] == 4:
                                nd = 2
                                cnt += 1
                        elif nd == 2 and ny> 0 and board[nx][ny-1] != 5 and board[nx][ny-1] != 3 and board[nx][ny-1] != 4:
                            ny -= 1
                            if board[nx][ny] == 1:
                                nd = 3
                                cnt += 1
                            elif board[nx][ny] == 2:
                                nd = 1
                                cnt += 1
                        elif nd == 3 and nx > 0 and board[nx-1][ny] != 5 and board[nx-1][ny] != 1 and board[nx-1][ny] != 4:
                            nx -= 1
                            if board[nx][ny] == 2:
                                nd = 0
                                cnt += 1
                            elif board[nx][ny] == 3:
                                nd = 2
                                cnt += 1
                        else:
                            cnt += 1
                            nd = (nd + 2) %4
                            if nd == 0:
                                if board[nx][ny] == 3:
                                    nd = 1
                                    cnt += 1
                                elif board[nx][ny] == 4:
                                    nd = 3
                                    cnt += 1
                            if nd == 1:
                                if board[nx][ny] == 1:
                                    nd = 0
                                    cnt += 1
                                elif board[nx][ny] == 4:
                                    nd = 2
                                    cnt += 1
                            if nd == 2:
                                if board[nx][ny] == 1:
                                    nd = 3
                                    cnt += 1
                                elif board[nx][ny] == 2:
                                    nd = 1
                                    cnt += 1
                            if nd == 3:
                                if board[nx][ny] == 2:
                                    nd = 0
                                    cnt += 1
                                elif board[nx][ny] == 3:
                                    nd = 2
                                    cnt += 1
                        #웜홀
                        if board[nx][ny] > 5:
                            w = worm[board[nx][ny]-6]
                            a = w[0]
                            b = w[1]
                            if a == [nx,ny]:
                                nx,ny = b
                            else:
                                nx,ny = a
                        
                    
                        if board[nx][ny] == -1 or [i,j] == [nx,ny]:
                            ret = cnt
                            break
                        
                    #print(i, j, direction, ret)
                    if score < ret:
                        score = ret
    print("#" + str(test_case) + " " + str(score))
