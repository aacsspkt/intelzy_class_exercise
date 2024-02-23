if __name__ == "__main__":
    # uninitialize = None
    # # equal operator
    # a = 1
    # b = 3
    # if a == b:
    #     print("a and b are same")

    # if a is b:
    #     print("a and b are same")

    # # not equal operator
    # if a != b: 
    #     print("not same")

    # if a is not b:
    #     print("also not same") 

    # # greater than, less than ,greaterthan or equal to lessthan or equals to
    # if a > b:
    #     print("a > b")

    # if a < b:
    #     print("a < b")

    # if a >= b:
    #     print("a >= b")

    # if a <= b:
    #     print("a <= b")

    # # logical operator
    # b = None
    # if a or b:
    #     print("one of them exists")

    # if a and b:
    #     print("both of them exists")

    # if not uninitialize:
    #     uninitialize = "intialized"

    # print(uninitialize)

    """
    write a program that takes marks and prints under which
    division it falls:
    80 and above: Distinction
    60-79: First Division
    50-59: Second Division
    40-49: Third Division
    39 and below: Fail

    """

    marks = int(input("Enter your marks:"))

    if marks >= 80:
        print("you got distinction")
    elif marks >= 60 and marks < 80:
        print("you got first division")
    elif marks >= 50 and marks < 60:
        print("you got second division")
    elif marks >= 40 and marks < 50:
        print("you got second division")
    else:
        print("you are failed")