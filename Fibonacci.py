def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

n = int(input("Please enter a number: "))

for fib in fibs():
  if n == fib:
    print ("Your number is a fibonacci number!")
    break
  if fib > n:
    print ("Your number is not a fibonacci number!")
    break
