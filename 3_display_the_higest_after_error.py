highest = None

while True:
    num = input("Enter a number: ") # ask the user for numbers
    if not num.isdigit():
        print(f"Highest number entered: {highest}") # print the highest when an error occured
        print("Invalid input. Goodbye!") 
        break
    num = int(num) # sets the highest value
    if highest is None or num > highest:
        highest = num
