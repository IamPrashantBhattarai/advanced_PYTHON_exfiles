# Use lambdas as in-place functions
# Small and Anonymous functions are known as lambda functions.
# It can be passed as argument where you need a function.


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    
    ftemps = [32, 65, 100, 212]

    # TODO: Use regular functions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # TODO: Use lambdas to accomplish the same thing
    """ Using the lymbda functions helps you to reduce the code as here we dont need to find the functions for conversion 
     We can simply use the lymbda expression."""
    print(list(map(lambda t:(t-32) * 5/9, ftemps)))
    print(list(map(lambda t:(t * 9/5) + 32, ctemps)))

if __name__ == "__main__":
    main()
