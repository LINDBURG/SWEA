import sys
sys.stdin = open("./sample_input.txt", "r")

class Board():
    def __init__(self, a, b):
        self.table = [[[] for _ in range(10)] for _ in range(10)]
        self.route_a = a
        self.route_b = b
        self.position_a = [0,0]
        self.position_b = [9,9]
        self.power = 0
        
    def set_AP(self, x, y, c, p, num):
        x -= 1
        y -= 1
        for i in range(10):
            for j in range(10):
                if abs(i-x) + abs(j-y) <= c:
                    self.table[i][j].append([p,num])

    def calc(self):
        a = self.position_a
        b = self.position_b
        for i in range(len(self.route_a)):
            self.add()
            self.move(a, self.route_a[i])
            self.move(b, self.route_b[i])
        self.add()

    def move(self, target, direction):
        if direction == 1:
            target[1] -= 1
        elif direction == 2:
            target[0] += 1
        elif direction == 3:
            target[1] += 1
        elif direction == 4:
            target[0] -= 1

    def add(self):
        a = self.position_a
        b = self.position_b
        pos_a = sorted(self.table[a[0]][a[1]])
        pos_b = sorted(self.table[b[0]][b[1]])
        max_power = 0
        #print(pos_a, pos_b)
        if len(pos_a) * len(pos_b) > 0:
            #print("case1")
            for pa in pos_a:
                for pb in pos_b:
                    tmp = pa[0] + pb[0]
                    if pa[1] == pb[1]:
                        tmp = pa[0]
                    if tmp > max_power:
                        max_power = tmp
        else:
            #print("case2")
            if len(pos_a) > 0:
                tmp = pos_a[-1][0]
            elif len(pos_b) > 0:
                tmp = pos_b[-1][0]
            else:
                tmp = 0
            if tmp > max_power:
                max_power = tmp

        #print(a, b, max_power)
        self.power += max_power

T = int(input())

for test_case in range(1, T + 1):
    m, ap = map(int, input().split(' '))
    a = list(map(int, input().split(' ')[:m]))
    b = list(map(int, input().split(' ')[:m]))
    board = Board(a, b)
    for i in range(ap):
        x, y, c, p = map(int, input().split(' '))
        board.set_AP(x, y, c, p, i)
    board.calc()
    print("#" + str(test_case) + ' ' + str(board.power))
    #print(board.table)