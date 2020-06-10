def generate_fibo(n):
    a = []
    while len(a) < n:
        if len(a) == 0 or len(a) == 1:
            a.append(1)
        else:
            a.append(a[len(a) - 1] + a[len(a) - 2])
    return a

n = int(input("Fibonacci numbers to generate: "))

print(generate_fibo(n))
