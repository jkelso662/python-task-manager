def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    n = int(input("Enter the number of terms: "))
    sequence = fibonacci_sequence(n)
    print("Fibonacci sequence:")
    for num in sequence:
        print(num)

if __name__ == "__main__":
    main()