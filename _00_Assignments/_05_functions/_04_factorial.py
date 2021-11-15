def factorial(num):  # function definition
    fact = 1
    for i in range(1, num + 1):  # for loop for finding factorial
        fact = fact * i
    return fact  # return factorial


number = int(input("Please enter any number to find factorial: "))
result = factorial(number)  # function call
print(f'The factorial of {number} is {result}')
