import module_with_main as mwm



def main():
    num = int(input("enter a radius of a circle: "))
    print(f"the area of a circle with a radius of {num} is {mwm.area(num)}")
    mwm.main()

    if __name__ == "__main__":
        main()