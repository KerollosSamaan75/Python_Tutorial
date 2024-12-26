def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = 5
    result = factorial(number)
    print(result)
    return result

main()
