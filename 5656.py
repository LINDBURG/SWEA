#import sys
#sys.stdin = open("sample_input.txt", 'r')
from copy import deepcopy

class Pinball():
    def __init__(self, N, W, H, board):
        self.N = N
        self.W = W
        self.H = H
        self.answer = 0
        self.remain = 0
        for row in board:
            for col in row:
                if col > 0:
                    self.remain += 1
        self.board = board
        self.run(self.board, 0, 0)
        self.answer = self.remain - self.answer

    def run(self, board, depth, cnt):
        if self.answer < cnt:
            #print("hit " + str(cnt))
            self.answer = cnt
        if depth < self.N:
            queue = []
            for y in range(self.W):
                for x in range(self.H):
                    if board[x][y] > 0:
                        queue.append([x,y])
                        break
            for x, y in queue:
                self.check = [[0 for _ in range(self.W)] for _ in range(self.H)]
                self.cnt = 0
                self.new_board = deepcopy(board)
                self.boom(x,y)
                self.go_down()
                #print(depth, x, y)
                self.run(self.new_board, depth + 1, cnt + self.cnt)

    def boom(self, x, y):
        board = self.new_board
        damage = board[x][y]
        for i in range(max(0,x-damage+1),min(self.H,x+damage)):
            if self.check[i][y] == 0 and board[i][y] > 0:
                self.cnt += 1
                self.check[i][y] = 1
                self.boom(i,y)
        for j in range(max(0,y-damage+1),min(self.W,y+damage)):
            if self.check[x][j] == 0 and board[x][j] > 0:
                self.cnt += 1
                self.check[x][j] = 1
                self.boom(x,j)

    def go_down(self):
        board = self.new_board
        check = self.check
        for y in range(self.W):
            for x in range(self.H):
                if check[x][y] == 1:
                    for i in range(x,-1,-1):
                        if i != 0:
                            board[i][y] = board[i-1][y]
                            board[i-1][y] = 0
                        else:
                            board[0][y] = 0


T = int(input())

for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = []
    for _ in range(H):
        line = list(map(int, input().split()))
        board.append(line)
    pinball = Pinball(N, W, H, board)
    print("#" + str(test_case) + " " + str(pinball.answer))
