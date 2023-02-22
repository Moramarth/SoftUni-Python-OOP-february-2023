"""
Fix the code below, so it returns the expected output.

Starting output:
global
outer: local
inner: nonlocal
outer: local
global

Expected output:
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!

"""


x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x  # missing nonlocal declaration for "x" variable
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # missing global declaration for "x" variable
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
