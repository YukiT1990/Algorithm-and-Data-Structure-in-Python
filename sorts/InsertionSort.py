from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('Insertion sort')
    num = int(input('The number of the elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    print(x)
    insertion_sort(x)


    print('Sorted x in ascending order.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

    print(x)


"""
Insertion sort
The number of the elements: 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
[6, 4, 3, 7, 1, 9, 8]
Sorted x in ascending order.
x[0] = 1
x[1] = 3
x[2] = 4
x[3] = 6
x[4] = 7
x[5] = 8
x[6] = 9
[1, 3, 4, 6, 7, 8, 9]
"""
