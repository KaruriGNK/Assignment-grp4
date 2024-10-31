def fib(n):
    #If n is 0, return a list with the first Fibonacci number
    if n == 0:
        return [0]

    #If n is 1, return a list with the first two Fibonacci numbers
    elif n == 1:
        return [0, 1]

    #for n greater than 1
    else:
        # Call the function recursively to get the Fibonacci sequence up to n-1
        lst = fib(n - 1)

        # Append the next Fibonacci number, which is the sum of the last two numbers in the list
        lst.append(lst[-1] + lst[-2])

        # Return the complete list of Fibonacci numbers up to n
        return lst
print(fib(8))
