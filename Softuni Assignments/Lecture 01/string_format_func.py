"""String format exercise."""

def main():
    """Collects and prints back person info."""
    # print("Enter name:")
    name = input()

    # print("Enter age:")
    age = input()

    # print("Enter town:")
    town = input()

    # print("Enter salary:")
    salary = float(input())

    sentence = f"{name} is {age} years old, is from {town} and makes ${salary}"
    sentence2 = "{} is {} years old, is from {} and makes ${}".format(name, age, town, salary)
    sentence3 = "%(a)s is %(b)s years old, is from %(c)s and makes $%(d)s" % {'a':name, 'b':age, 'c':town, 'd':salary }

    print(sentence)
    print(sentence2)
    print(sentence3)

if __name__ == '__main__':
    main()
