class Lock():
    def __init__(self, N, K, line):
        self.dist = N//4
        self.N = N
        self.K = K
        self.line = line + line[:self.dist]
        self.num = []
        self.make()
        self.trans()

    def make(self):
        for i in range(self.N):
            self.num.append(self.line[i:i+self.dist])
        self.num = list(set(self.num))

    def trans(self):
        self.num = list(map(lambda x:int(x,16), self.num))
        self.num.sort(reverse = True)
        self.answer = self.num[self.K-1]

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    line = input().strip()
    lock = Lock(N, K, line)
    print("#" + str(test_case) + " " + str(lock.answer))
