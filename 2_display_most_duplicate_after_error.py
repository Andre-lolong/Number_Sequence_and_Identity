number_counts = {}

while True:
    try:
        user_input = input("Enter a number: ") # get numbers from the user
        number = int(user_input)
        # count and identify the number
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1
    except ValueError:
        print("Invalid input. Exiting program.") # stop when error occured
        break

if number_counts:
    most_frequent = None
    max_count = 0
    for num in number_counts:
        if number_counts[num] > max_count:
            max_count = number_counts[num]
            most_frequent = num
    print(f"The number with the most duplicates is: {most_frequent}")
