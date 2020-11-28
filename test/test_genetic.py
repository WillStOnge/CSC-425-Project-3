import unittest
from ml_algorithms import Genetic

class TestGeneticAlgorithm(unittest.TestCase):
    def test(self):
        start_codes = list()
        correct_code = """def sequentialSearch(alist, item):
        pos = 0
        found = False
        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos+1
        return found"""
        start_codes.append("""def sequentialSearch(alist, item):
        pos = 0
        found = False
        while pos < len(alist) and not found:
            if alist[pos] != item:
                found = True
            else:
                pos = pos*2
        return found""")
        start_codes.append("""def sequentialSearch(alist, item):
        pos = 0
        found = False
        while pos > len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos+1
        return found""")

        Genetic(start_codes, correct_code).execute()
