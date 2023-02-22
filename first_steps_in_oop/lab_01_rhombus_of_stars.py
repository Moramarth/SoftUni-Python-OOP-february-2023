"""" Create a program that reads a positive integer N as input and prints on the console a rhombus with size n: """


def rhombus_pattern(size):
    for i in range(1, size + 1):
        print(" " * (size - i), "* " * i)
    for i in range(size - 1, -1, -1):
        print(" " * (size - i), "* " * i)


size_number = int(input())
rhombus_pattern(size_number)
