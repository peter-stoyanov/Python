"""Range function."""

def main():
    """Generates numbers by user input."""
    start = int(input())
    end = int(input())
    step = int(input())
    for number in range(start, end, step):
        print(number)

if __name__ == '__main__':
    main()
