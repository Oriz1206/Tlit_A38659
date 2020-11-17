Fibonacci_cache = {}
Alist = []
m = int(input("nhap tu ban phim so m :"))
def Fibonacci(n):
    if n in Fibonacci_cache:
        return Fibonacci_cache[n]
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n > 1:
        value = Fibonacci(n - 1) + Fibonacci(n - 2)
    Fibonacci_cache[n] = value
    return value
for n in range(1,100):
    print(Fibonacci(n))