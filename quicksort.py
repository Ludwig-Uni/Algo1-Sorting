import random


def quickSort(a):
    """
    Sortiert das gegebene Array `a` mit dem Quicksort Algorithmus
    """
    quicksort_worker(a, 0, len(a) - 1)


def quicksort_worker(a, lo, hi):
    """
    Worker für Quicksort, arbeitet rekursiv bis das Array sortiert ist
    """

    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(a, lo, hi)
        quicksort_worker(a, lo, p)
        quicksort_worker(a, p+1, hi)


def partition(a, lo, hi):
    """
    Wählt das mittlere Element des Arrays (zwischen den Grenzen lo und hi)
    als Pivot-Element, sortiert alle x > pivor rechts und alle x < pivot links davon
    und gibt den Index des Pivot-Elements zurück.
    """
    pivot = a[(lo + hi) // 2]
    i = lo
    j = hi

    while True:
        while a[i] < pivot:
            i += 1
        
        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
