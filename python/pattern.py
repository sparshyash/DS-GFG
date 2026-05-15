def print_pascal_triangle(n):
    for i in range(n):
        print(" " * (n - i), end="")
        value = 1
        for j in range(i + 1):
            print(value, end=" ")
            value = value * (i - j) // (j + 1)
        print()

n = 4
print_pascal_triangle(n)
