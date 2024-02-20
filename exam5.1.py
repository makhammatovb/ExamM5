def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


n = int(input("Number: "))

gen = fibonacci()
seq = []
for i in range(n):
    num = next(gen)
    seq.append(num)

print(seq)
