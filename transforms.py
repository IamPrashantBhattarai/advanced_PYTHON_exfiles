# use transform functions like sorted, filter, map



from operator import truediv
from re import A


def filterFunc(x):
    # This filter func helps to filter the odd ones and only gives true to the even values. 
    if x % 2 == 0:
        return True
    return False
    

def filterFunc2(x):
    if x.isupper():
        return True
    return False


def squareFunc(x):
    return x*x


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >=80 and x<=90):
        return "B"
    elif (x >=70 and x<=80):
        return "C"
    elif (x >=60 and x<=70):
        return "D"
    else:
        return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    evens = list(filter(filterFunc , nums))
    print(evens)


    # TODO: use filter on non-numeric sequence
    uppers = list(filter(filterFunc2 , chars))
    print(uppers)

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc , nums))
    print(squares)


    # TODO: use sorted and map to change numbers to grades
    # grades = sorted(grades)
    # print(grades)
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()
