# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    reasult= 0
    for arg in args:
        reasult += arg
    return reasult



def main():
    # TODO: pass different arguments
    print(addition(10,20,30))
    print(addition(1,2,3,4))

    # TODO: pass an existing list
    myList = [10,20,30]
    print(addition(*myList))


if __name__ == "__main__":
    main()
