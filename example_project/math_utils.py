def calculate_average(numbers):
    total = sum(numbers)
    # BUG: No check for empty list, will cause ZeroDivisionError
    average = total / len(numbers)
    return average

def process_data(data_list):
    print("Processing data...")
    try:
        avg = calculate_average(data_list)
        print(f"Average: {avg}")
    except Exception as e:
        # We will use this trace for testing
        raise e

if __name__ == "__main__":
    # Test with empty list to trigger error
    process_data([])
