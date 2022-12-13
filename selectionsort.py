from math import inf, nan


def selectionSort(a):
    """
    Sortiert das gegebene Array `a` mit dem Selection-Sort Algorithmus
    """
    result = []
    for i in range(len(a)):
        min_index = nan
        minimum = inf
        
        # Suche das minimale Element im Rest des Arrays
        for j in range(i, len(a)):
            if a[j] < minimum:
                minimum = a[j]
                min_index = j
        
        # Vertausche das aktuelle Element mit dem gefundenen minimalen Element
        a[i], a[min_index] = a[min_index], a[i]
