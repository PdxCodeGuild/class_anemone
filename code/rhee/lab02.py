
numbers = 0
count = 0
average = 0
while True:
    num = input("Enter a number to add to the list or enter 'done' to quit: ")
    if num == '':
        print("Ending sequence!")
        break
    numbers += int(num)
    count += 1
average = numbers / count

print(f"Sum of all number in {numbers} and the average is {average} ")
