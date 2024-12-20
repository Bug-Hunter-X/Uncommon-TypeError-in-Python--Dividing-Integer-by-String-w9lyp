def function_with_uncommon_error(x):
    try:
        if isinstance(x, str):
            raise TypeError("Cannot divide by a string")
        result = 10 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

#Example of an uncommon error
#The following code will raise a TypeError because we are trying to divide a integer by a string
result = function_with_uncommon_error("hello")
print(f"Result: {result}")
#Example of a common error, ZeroDivisionError
result = function_with_uncommon_error(0)
print(f"Result: {result}")
#Example of a normal case
result = function_with_uncommon_error(2)
print(f"Result: {result}")
