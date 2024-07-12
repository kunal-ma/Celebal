# Create lower triangular, upper triangular and pyramid containing the "*" character

# Function to create lower triangular
def lower_triangle(n):
    print()
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()

# Function to create upper triangular
def upper_triangle(n):
    print()
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()

# Function to create pyramid
def pyramid(n):
    print()
    for i in range(n):
        for j in range(n-i):
            print(end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()

# Main function
def main():
    n = int(input("Enter the number of rows: "))
    print("\nLower Triangular")
    lower_triangle(n)
    print("\nUpper Triangular")
    upper_triangle(n)
    print("\nPyramid")
    pyramid(n)

# Main function call
if __name__ == "__main__":
    main()