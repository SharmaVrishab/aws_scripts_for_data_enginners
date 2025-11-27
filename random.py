import sys


def main():
    # Check if command-line arguments were provided
    print(sys.argv)
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        print(f"You entered (from argv): {user_input}")
    else:
        # If no arguments, prompt for interactive input
        user_input = input("Enter something: ")
        print(f"You entered (from input): {user_input}")
    sys.exit(0)


if __name__ == "__main__":
    main()
