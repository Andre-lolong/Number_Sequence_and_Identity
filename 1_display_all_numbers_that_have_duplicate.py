def display_duplicate_numbers():
    numbers = []
    for i in range(10):
            num = int(input(f"Enter value for number {i + 1}: ")) # ask the user for numbers
            numbers.append(num)

    duplicate_numbers = [num for num in numbers if numbers.count(num) != 1] # check for duplicate
    if unique_numbers: # display duplicated numbers
          print(f"Here are the list of numbers that do have duplicates: {duplicate_numbers}")    
    else:
          print("No duplicate numbers entered")

display_duplicate_numbers()