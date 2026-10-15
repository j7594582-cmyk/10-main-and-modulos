pi = 3.1459


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def circumference(radius):
    return 2 * pi * radius


def area(radius:float) -> float:
    """
    takes the radius of a circle and returns the area
    """
    return pi * (radius ** 2)


def main():
        print("just testing")
        print(area(7))
        print(pi)
        #every python file (aka module) has a sspecial built in variable called __name__
        #if you run the file directly, __name__ is set to __main__
        #if you import the file, __name__ becomes the name of that script
        print(__name__)
        print("just testing")
if __name__ == "__main__":
    main()