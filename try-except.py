def divide():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        return num1 / num2
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)
    except:
        print("Something went wrong")


result = divide()
print(result)