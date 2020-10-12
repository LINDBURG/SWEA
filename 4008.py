import sys
sys.stdin = open("sample_input.txt", 'r')

class Number():
    def __init__(self, N, arr, numbers):
        self.N = N
        self.arr = list(arr)
        self.min = 100000000
        self.max = -100000000
        
        self.process(numbers[0], numbers[1:])

        self.answer = self.max - self.min
        
    def process(self, a, numbers):
        if not numbers:
            if self.max < a:
                self.max = a
            if self.min > a:
                self.min = a
            return 0
        
        b = numbers.pop(0)
        for i in range(4):
            if self.arr[i] > 0:
                self.arr[i] -= 1
                c = self.calc(a, b, i)
                self.process(c, numbers[:])
                self.arr[i] += 1
        
    def calc(self, a, b, num):
        if num == 0:
            return a + b
        elif num == 1:
            return a - b
        elif num == 2:
            return a * b
        else:
            return int(a / b)
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    calc = map(int, input().split())
    arr = list(map(int, input().split()))
    number = Number(N, calc, arr)
    print("#" + str(test_case) + " " + str(number.answer))
