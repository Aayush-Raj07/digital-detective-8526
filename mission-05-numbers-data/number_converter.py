def main():
    while True:
        raw = input("Enter a positive integer (or 'q' to quit): ").strip()
        if raw.lower() == 'q':
            print("Goodbye!")
            break
        try:
            n = int(raw)
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            print(f"Decimal:     {n}")
            print(f"Binary:      {bin(n)}")
            print(f"Hexadecimal: {hex(n)}")
            print()
        except ValueError:
            print("That does not look like a whole number. Please try again.")

if __name__ == "__main__":
    main()
