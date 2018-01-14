"""Execution time"""

import timeit

def main():
    """Execution time methods"""

    # For loop
    time_for_loop = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(time_for_loop)

    # List comprehension
    time_list_comprehension = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
    print(time_list_comprehension)

    # Map()
    time_map = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
    print(time_map)

if __name__ == '__main__':
    main()
