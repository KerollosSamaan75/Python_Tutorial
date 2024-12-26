def calculate_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average

def main():
    numbers = [10, 20, 30, 40, 50]  # Example list
    result = calculate_average(numbers)
    print("The average is:", result)

main()
