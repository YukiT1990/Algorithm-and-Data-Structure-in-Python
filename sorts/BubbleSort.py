# Bubble sort
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

def bubble_sort_verbose(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n - 1):
        print(f'{i + 1}th path')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'comparison: {ccnt} times.')
    print(f'exchange: {scnt} times.')

def bubble_sort_improved(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        exchange = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        if exchange == 0:
            break

def bubble_sort_improved_verbose(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n - 1):
        print(f'{i + 1}th path')
        exchange = 0
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        if exchange == 0:
            break
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'comparison: {ccnt} times.')
    print(f'exchange: {scnt} times.')

def bubble_sort_improved2(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last

def bubble_sort_improved2_verbose(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    k = 0
    while k < n - 1:
        print(f'{k + 1}th path')
        last = n - 1
        for j in range(n - 1, k, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'comparison: {ccnt} times.')
    print(f'exchange: {scnt} times.')


if __name__ == '__main__':
    print('Bubble sort')
    num = int(input('The number of the elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    print(x)
    # bubble_sort(x)
    # bubble_sort_verbose(x)
    # bubble_sort_improved_verbose(x)
    bubble_sort_improved2_verbose(x)


    print('Sorted x in ascending order.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

    print(x)

"""
The number of the elements: 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
[6, 4, 3, 7, 1, 8, 9]
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

"""
Bubble sort
The number of the elements: 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
[6, 4, 3, 7, 1, 9, 8]
1th path
 6   4   3   7   1   9 + 8
 6   4   3   7   1 - 8   9
 6   4   3   7 + 1   8   9
 6   4   3 + 1   7   8   9
 6   4 + 1   3   7   8   9
 6 + 1   4   3   7   8   9
 1   6   4   3   7   8   9
2th path
 1   6   4   3   7   8 - 9
 1   6   4   3   7 - 8   9
 1   6   4   3 - 7   8   9
 1   6   4 + 3   7   8   9
 1   6 + 3   4   7   8   9
 1   3   6   4   7   8   9
3th path
 1   3   6   4   7   8 - 9
 1   3   6   4   7 - 8   9
 1   3   6   4 - 7   8   9
 1   3   6 + 4   7   8   9
 1   3   4   6   7   8   9
4th path
 1   3   4   6   7   8 - 9
 1   3   4   6   7 - 8   9
 1   3   4   6 - 7   8   9
 1   3   4   6   7   8   9
5th path
 1   3   4   6   7   8 - 9
 1   3   4   6   7 - 8   9
 1   3   4   6   7   8   9
6th path
 1   3   4   6   7   8 - 9
 1   3   4   6   7   8   9
comparison: 21 times.
exchange: 8 times.
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

"""
Bubble sort improved
The number of the elements: 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
[6, 4, 3, 7, 1, 9, 8]
1th path
 6   4   3   7   1   9 + 8
 6   4   3   7   1 - 8   9
 6   4   3   7 + 1   8   9
 6   4   3 + 1   7   8   9
 6   4 + 1   3   7   8   9
 6 + 1   4   3   7   8   9
 1   6   4   3   7   8   9
2th path
 1   6   4   3   7   8 - 9
 1   6   4   3   7 - 8   9
 1   6   4   3 - 7   8   9
 1   6   4 + 3   7   8   9
 1   6 + 3   4   7   8   9
 1   3   6   4   7   8   9
3th path
 1   3   6   4   7   8 - 9
 1   3   6   4   7 - 8   9
 1   3   6   4 - 7   8   9
 1   3   6 + 4   7   8   9
 1   3   4   6   7   8   9
4th path
 1   3   4   6   7   8 - 9
 1   3   4   6   7 - 8   9
 1   3   4   6 - 7   8   9
comparison: 18 times.
exchange: 8 times.
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

"""
Bubble sort improved 2
The number of the elements: 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
[6, 4, 3, 7, 1, 9, 8]
1th path
 6   4   3   7   1   9 + 8
 6   4   3   7   1 - 8   9
 6   4   3   7 + 1   8   9
 6   4   3 + 1   7   8   9
 6   4 + 1   3   7   8   9
 6 + 1   4   3   7   8   9
 1   6   4   3   7   8   9
2th path
 1   6   4   3   7   8 - 9
 1   6   4   3   7 - 8   9
 1   6   4   3 - 7   8   9
 1   6   4 + 3   7   8   9
 1   6 + 3   4   7   8   9
 1   3   6   4   7   8   9
3th path
 1   3   6   4   7   8 - 9
 1   3   6   4   7 - 8   9
 1   3   6   4 - 7   8   9
 1   3   6 + 4   7   8   9
 1   3   4   6   7   8   9
4th path
 1   3   4   6   7   8 - 9
 1   3   4   6   7 - 8   9
 1   3   4   6 - 7   8   9
 1   3   4   6   7   8   9
comparison: 18 times.
exchange: 8 times.
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
