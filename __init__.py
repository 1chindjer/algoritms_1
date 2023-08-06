# Сортировка массива кучей (HeapSort)
from enum import Enum
import random


def arraygen ():
    ''' Создаем массив или рандомом, или пользовательским вводом
      с указанием размерности массива
    '''
    class Menue1(Enum):
        AUTO = 'A'
        MANUAL = 'M'

    while True:
        print('Введите количество элементов массива')
        try:
            n = int(input())
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    while True:
        print("Желаете автоматом генерировать массив (A), или укажете вручную (M), введите A/M")
        temp = str(input().upper())
        if temp == Menue1.AUTO.value:
            print("Массив создан автоматом")
            arr = [random.randint(1, 100) for _ in range(n)]
            return arr
            
        elif temp == Menue1.MANUAL.value:
            print("Вам будет предложено ввести массив вручную")
            arr = []
            for i in range(n):
                while True:
                    try:
                        value = int(input(f"Введите элемент {i + 1}: "))
                        arr.append(value)
                        break
                    except ValueError:
                        print("Пожалуйста, введите корректное число.")
            return arr

        else:
            print('Вы указали некорректный способ формирования массива. Попробуйте снова.')


def swap(arr, i, j):
    """
    Меняет местами элементы с индексами i и j в массиве arr.
    """
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    n = len(arr)

    # Построение максимальной кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # перемещаем текущий корень в конец
        heapify(arr, i, 0)  # вызываем heapify на уменьшенной куче

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)


array = arraygen()
print("Ваш массив:", array)

heapSort (array)
print ("сортированный массив", array)