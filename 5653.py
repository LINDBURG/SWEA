#import sys
#sys.stdin = open("sample_input.txt", 'r')

class Plate():
    def __init__(self, N, M, K, arr):
        self.base = K//2 + 2
        self.board = [[0 for _ in range(self.base*2 + M)] for _ in range(self.base*2 + N)]
        self.disabled = [[] for _ in range(11)]
        self.enabled = []
        self.answer = 0
        
        for i in range(N):
            for j in range(M):
                self.board[self.base+i][self.base+j] = arr[i][j]
                if arr[i][j] > 0:
                    self.disabled[arr[i][j]-1].append([arr[i][j],self.base+i, self.base+j])
                    
        for _ in range(K):
            self.calc_disabled()
            self.check()
            self.calc_enabled()

    def check(self):
        answer = sum(map(len,self.disabled))
        answer += len(self.enabled)
        self.answer = answer
            
    def calc_disabled(self):
        disabled = self.disabled.pop(0)
        self.disabled.append([])
        disabled.sort(reverse = True)
        
        for cost, x, y in disabled:
            self.enabled.append([cost,cost,x,y])
            
    def calc_enabled(self):
        self.enabled.sort(reverse = True)
        remain = []
        for cost, time, x, y in self.enabled:
            for i, j in [[0,1],[0,-1],[-1,0],[1,0]]:
                if self.board[x+i][y+j] == 0:
                    self.board[x+i][y+j] = cost
                    self.disabled[cost].append([cost, x+i, y+j])
            if time > 1:
                remain.append([cost,time-1,x,y])
        
        self.enabled = remain
        
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    plate = Plate(N, M, K, arr)
    print("#" + str(test_case) + " " + str(plate.answer))
