numbers = []

while True:
    num = input("Enter a number: ") # get numbers
    if not num.isdigit(): # stop when error occcurs
        print("Numbers entered in order from lowest to highest:")
        print(sorted(numbers, reverse=True)) # arrange # print
        print("Invalid input. Farewell program")
        break
    numbers.append(int(num))  # get the values entered
