#(1)
a = 10
b = 20

# TODO
if a>b:
    while b!=0:
        a, b = b, a % b      
    print(f"最大公約数: {a}")
if a<=b:
    while a!=0:
        b, a = a, b % a
    print(f"最大公約数: {b}")
#(2)
a = 14
b = 91

# TODO
if a>b:
    while b!=0:
        a, b = b, a % b      
    print(f"最大公約数: {a}")
if a<=b:
    while a!=0:
        b, a = a, b % a
    print(f"最大公約数: {b}")

#(3)
a = 91
b = 14

# TODO
if a>b:
    while b!=0:
        a, b = b, a % b      
    print(f"最大公約数: {a}")
if a<=b:
    while a!=0:
        b, a = a, b % a
    print(f"最大公約数: {b}")