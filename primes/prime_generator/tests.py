from django.test import TestCase
import unittest

from .views import sieve_eratosthenes,normal_method2,trial_division

# Create your tests here.
class PrimeGeneratorTest(unittest.TestCase):

    def test(self):
        self.assertEqual(sieve_eratosthenes(2, 10), [2, 3, 5, 7])
        self.assertEqual(trial_division(1, 1), [], "Handles lower bound of 1")
        self.assertEqual(normal_method2(30, 50), [31, 37, 41, 43, 47])

if __name__ == "__main__":
    unittest.main()