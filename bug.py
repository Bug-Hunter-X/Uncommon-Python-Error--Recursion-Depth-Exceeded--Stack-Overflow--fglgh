def function_with_uncommon_error(n):
    if n == 0:
        return 0  # This is fine
    elif n == 1:
        return 1  # This is fine
    else:
        return function_with_uncommon_error(n - 1) + function_with_uncommon_error(n - 2) # Uncommon error: Stack Overflow for large n

result = function_with_uncommon_error(35) # Example causing stack overflow