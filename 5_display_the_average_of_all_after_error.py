# List to store entered numbers
numbers = []

while True:
    try:
        # Ask user to enter a number
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
    except ValueError:
        print("Invalid input. Babababyeeee...") # stop when error occurs
        break

if numbers:
# get the average of all entered numbers
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")
