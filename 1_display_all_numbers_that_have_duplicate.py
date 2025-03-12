def display_unique_numbers():
    numbers = []
    for i in range(10):
            num = int(input(f"Enter value for number {i + 1}: ")) # ask the user for numbers
            numbers.append(num)

    unique_numbers = [num for num in numbers if numbers.count(num) != 1] # check for duplicate
    if unique_numbers: # display duplicated numbers
          print(f"Here are the list of numbers that do not have duplicates: {unique_numbers}")    
    else:
          print("No unique numbers entered")

display_unique_numbers()