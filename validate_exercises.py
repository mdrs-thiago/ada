def test_q1(f):
    n = 1
    # Test for the find_highest_score function
    leaderboard = [("John", 1000, 5), ("Alice", 1500, 4), ("Bob", 1200, 6)]
    expected_result = ("Alice", 1500, 4)
    try:
        result = f(leaderboard)
        assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1


    # Test with different leaderboard data
    leaderboard2 = [("Tom", 500, 3), ("Jerry", 800, 2), ("Spike", 300, 1)]
    expected_result2 = ("Jerry", 800, 2)
    try:
        result2 = f(leaderboard2)
        assert result2 == expected_result2, f"Expected: {expected_result2}, but got: {result2}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1

def test_q2(f):
    n = 1
    phonebook = {"Alice": "123-456-7890", "Bob": "987-654-3210"}

    # Test for looking up an existing contact
    expected_result1 = "Contact found: Alice - 123-456-7890"
    try:
        result1 = f(phonebook, "Alice", "123-456-7890")
        assert result1 == expected_result1, f"Expected: {expected_result1}, but got: {result1}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1

    # Test for adding a new contact
    expected_result2 = "Contact added: Charlie - 555-123-4567"
    try:
        result2 = f(phonebook, "Charlie", "555-123-4567")
        assert result2 == expected_result2, f"Expected: {expected_result2}, but got: {result2}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1
    # Check if the new contact is added to the phone book
    try:
        assert phonebook["Charlie"] == "555-123-4567", f"Expected: {phonebook['Charlie']}, but got: {result2}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1
    # Test with another contact lookup
    expected_result3 = "Contact added: David - 999-888-7777"
    try:
        result3 = f(phonebook, "David", "999-888-7777")
        assert result3 == expected_result3, f"Expected: {expected_result3}, but got: {result3}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1
    # Check if the new contact is added to the phone book
    try:
        assert phonebook["David"] == "999-888-7777", f"Expected: {phonebook['David']}, but got: {result3}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1

def test_q3(f):
    n = 1
    
    # Test for process_data_files function
    input_files = ["input_file1.txt", "input_file2.txt"]  # Provide appropriate input file paths for testing
    output_file = "output_file.txt"  # Provide appropriate output file path for testing

    # Create and write data to the input files for testing
    data1 = "hello world"
    data2 = "python is awesome"
    with open(input_files[0], 'w') as file1, open(input_files[1], 'w') as file2:
        file1.write(data1)
        file2.write(data2)

    # Call the function to process data from input files and write to the output file
    try:
        f(input_files, output_file)

        # Read the contents of the output file and perform assertions on processed data
        with open(output_file, 'r') as outfile:
            processed_data = outfile.read()
            expected_result = f"{data1.upper()}{data2.upper()}"
            try:
                assert processed_data == expected_result, f"Expected: {expected_result}, but got: {processed_data}"
            except Exception as e:
                print(e)
            else:
                print(f'Passou no {n}º teste!')
                n += 1
    except Exception as e:
        print(e)

def test_q4(f):
    n = 1
    def double_value(numbers):
        return [num * 2 for num in numbers]

    def square_value(numbers):
        return [num ** 2 for num in numbers]

    # Test for apply_operation function
    numbers = [1, 2, 3, 4, 5]

    # Test with doubling the values
    expected_double = [2, 4, 6, 8, 10]
    try:
        result_double = f(numbers, double_value)
        assert result_double == expected_double, f"Expected: {expected_double}, but got: {result_double}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1
    # Test with squaring the values
    expected_square = [1, 4, 9, 16, 25]
    try:
        result_square = f(numbers, square_value)
        assert result_square == expected_square, f"Expected: {expected_square}, but got: {result_square}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1

def test_q5(f):
    # Test for calculate_average function
    n = 1
    numbers = [10, 20, 30, 40, 50]

    # Test with valid input
    expected_result = 30
    try:
        result = f(numbers)
        assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1
    # Test with empty list (division by zero)
    empty_list = []
    expected_result_empty_list = 0
    try:
        result_empty_list = f(empty_list)
        assert result_empty_list == expected_result_empty_list, f"Expected: {expected_result_empty_list}, but got: {result_empty_list}"
    except Exception as e:
        print(e)
    else:
        print(f'Passou no {n}º teste!')
        n += 1
    # Test with invalid input (non-numeric value)
    invalid_input = [10, 20, "30", 40, 50]
    try:
        result_invalid_input = f(invalid_input)
    except ValueError as e:
        assert str(e) == "Invalid input. Please provide a list of numbers."
    else:
        raise AssertionError("Expected a ValueError, but no exception was raised.")
