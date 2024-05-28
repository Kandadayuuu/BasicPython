#問1
#(1)
# TODo
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        n += 6
        return True
n=61
if is_prime(n):
    print(f"{n}は素数です。")
else:
    print(f"{n}は素数ではありません。")

#(2)
# TODo
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        n += 6
        return True
n=10
if is_prime(n):
    print(f"{n}は素数です。")
else:
    print(f"{n}は素数ではありません。")  