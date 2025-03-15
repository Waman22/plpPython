# Example of a for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love {fruit}!")
    

# Example of a for loop with range
for number in range(1, 6):  # Loops from 1 to 5
    print(f"Number: {number}") 

# Example of a while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter
    
    
# Example of loop controls: break and continue
for number in range(1, 10):  # Loop through numbers 1 to 9
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip the rest of the loop body for even numbers
    print(f"Processing number: {number}")
    
# Traditional loop
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]