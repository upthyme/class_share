def f(func):
    print("Outside")
    print(type(func))
    print(func)

    def inside():
        print("Inside")
        func("Passed a string in inside")

    inside()
    string = func("Passed a string in outside")
    print(string)
    print("End")


def foo(stringex):
    print("Foo")
    print(stringex)
    return(stringex)

f(foo)
print()
#f(foo("Second Foo String")) # Dont do this because we get a string 