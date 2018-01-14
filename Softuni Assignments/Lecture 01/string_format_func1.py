"""String format exercise."""

def main():
    """Collects and prints back person info."""
    # print("Enter name:")
    name = input()

    # print("Enter age:")
    age = int(input())

    # print("Enter town:")
    town = input()

    # print("Enter salary:")
    salary = float(input())

    age_range = 'teen' if age < 18 else ('elder' if age > 70 else 'adult')
    salary_range = 'low' if salary < 500 else ('high' if salary > 2000 else 'medium')

    print('Name: {}'.format(name))
    print('Age: {}'.format(age))
    print('Town: {}'.format(town))
    print('Salary: ${0:.2f}'.format(salary))
    print('Age range: {}'.format(age_range))
    print('Salary range: {}'.format(salary_range))

if __name__ == '__main__':
    main()
