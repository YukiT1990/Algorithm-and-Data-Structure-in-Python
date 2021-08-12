from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

if __name__ == '__main__':
    print('Selection sort')
    num = int(input('The number of the elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    print(x)
    selection_sort(x)


    print('Sorted x in ascending order.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

    print(x)
