class Fibonacci:
    def __init__(self):
        self.memo = {}
        # self.num = num

    def fib(self, num):
        if num in self.memo:
            return self.memo[num]
        if num == 0:
            self.memo[num] = 0
            return 0
        elif num == 1:
            self.memo[num] = 1
            return 1
        else:
            self.memo[num] = self.fib(num-1) + self.fib(num-2)
            print(self.memo)
            return self.memo[num]

if __name__ == "__main__":
    f = Fibonacci()
    print(f.fib(6))
