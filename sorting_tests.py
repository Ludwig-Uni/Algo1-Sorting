import unittest
import selectionsort
import quicksort
import random

class SelectionSortTests(unittest.TestCase):
    def test_empty(self):
        """"
        Das leere Array sollte sortiert immer noch leer sein.
        """
        a = []
        selectionsort.selectionSort(a)
        self.assertEqual(a, [])

    def test_one_element(self):
        """"
        Das einelementige Array ist bereits sortiert
        """
        a = [42]
        selectionsort.selectionSort(a)
        self.assertEqual(a, [42])

    def test_multiple_elements(self):
        """
        Überprüfe, ob der Algorithmus ein Array sortiert
        """
        a = [43, 6, 1, 67, -2, -8, 0, 9]
        selectionsort.selectionSort(a)
        self.assertEqual(a, [-8, -2, 0, 1, 6, 9, 43, 67])

    def test_equal_elements(self):
        """
        Mehrere identische Elemente sollten kein Problem für die Sortierung darstellen
        """
        a = [1, 2, 3, 1, 2, 3, 3, 2, 1]
        selectionsort.selectionSort(a)
        self.assertEqual(a, [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_random_arrays(self):
        """
        Teste 1000 zufällige Arrays der Länge 100 und vergleiche sie mit dem Ergebnis der eingebauten sorted-Funktion
        """
        for i in range(1000):
            a = [random.randint(-500, 500) for elem in range(100)]
            solution = sorted(a)

            selectionsort.selectionSort(a)
            self.assertEqual(a, solution)


class QuickSortTests(unittest.TestCase):
    def test_empty(self):
        """"
        Das leere Array sollte sortiert immer noch leer sein.
        """
        a = []
        quicksort.quickSort(a)
        self.assertEqual(a, [])

    def test_one_element(self):
        """"
        Das einelementige Array ist bereits sortiert
        """
        a = [42]
        quicksort.quickSort(a)
        self.assertEqual(a, [42])

    def test_multiple_elements(self):
        """
        Überprüfe, ob der Algorithmus ein Array sortiert
        """
        a = [43, 6, 1, 67, -2, -8, 0, 9]
        quicksort.quickSort(a)
        self.assertEqual(a, [-8, -2, 0, 1, 6, 9, 43, 67])

    def test_equal_elements(self):
        """
        Mehrere identische Elemente sollten kein Problem für die Sortierung darstellen
        """
        a = [1, 2, 3, 1, 2, 3, 3, 2, 1]
        quicksort.quickSort(a)
        self.assertEqual(a, [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_random_arrays(self):
        """
        Teste 1000 zufällige Arrays der Länge 100 und vergleiche sie mit dem Ergebnis der eingebauten sorted-Funktion
        """
        for i in range(1000):
            a = [random.randint(-500, 500) for elem in range(100)]
            solution = sorted(a)

            quicksort.quickSort(a)
            self.assertEqual(a, solution)
