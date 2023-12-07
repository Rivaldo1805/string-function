def project():
    s = int(input("ENTER THE FUNCTION NAME: 1.swapcase() 2.strip() 3.islower() 4.replace() 5.zfill() 6.title() 7.count() 8.isupper() 9.splitlines() 10.isdecimal()"))

    if s == 1:
        print("YOU'RE PERFORMING SWAPCASE FUNCTION")
        input_str = input("enter the string: ")
        result_str = input_str.swapcase()
        print("Result:", result_str)

    elif s == 2:
        print("YOU'RE PERFORMING STRIP FUNCTION")
        input_str = input("enter the string: ")
        result_str = input_str.strip()
        print("Result:", result_str)

    elif s == 3:
        print("YOU'RE PERFORMING ISLOWER FUNCTION")
        input_str = input("enter the string: ")
        result = input_str.islower()
        print("Result:", result)

    elif s == 4:
        print("YOU'RE PERFORMING REPLACE FUNCTION")
        input_str = input("enter the string: ")
        old_str = input("enter the substring to replace: ")
        new_str = input("enter the new substring: ")
        result = input_str.replace(old_str, new_str)
        print("Result:", result)

    elif s == 5:
        print("YOU'RE PERFORMING ZFILL FUNCTION")
        input_str = input("enter the string: ")
        width = int(input("enter the width for zfill: "))
        result = input_str.zfill(width)
        print("Result:", result)

    elif s == 6:
        print("YOU'RE PERFORMING TITLE FUNCTION")
        input_str = input("enter the string: ")
        result = input_str.title()
        print("Result:", result)

    elif s == 7:
        print("YOU'RE PERFORMING COUNT FUNCTION")
        input_str = input("enter the string: ")
        sub_str = input("enter the substring to count: ")
        result = input_str.count(sub_str)
        print("Result:", result)

    elif s == 8:
        print("YOU'RE PERFORMING ISUPPER FUNCTION")
        input_str = input("enter the string: ")
        result = input_str.isupper()
        print("Result:", result)

    elif s == 9:
        print("YOU'RE PERFORMING SPLITLINES FUNCTION")
        input_str = input("enter the string: ")
        result = input_str.splitlines()
        print("Result:", result)

    elif s == 10:
        print("YOU'RE PERFORMING ISDECIMAL FUNCTION")
        input_str = input("enter the string: ")
        result = input_str.isdecimal()
        print("Result:", result)

    else:
        print("Invalid choice.")

    continue_choice = input("DO YOU WANT TO CONTINUE? (Yes/No): ")

    if continue_choice.lower() == "no":
        print("Program stopped.")
    else:
        project()


# Call the function
project()
