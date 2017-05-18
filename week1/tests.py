import random
import unittest

import time

from week1.matrix import Matrix
from week1.quick_sort import quick_sort


class TestMatrix(unittest.TestCase):
    def test_create(self):
        self.assertRaises(TypeError, Matrix, 1)
        self.assertRaises(TypeError, Matrix, 'asdf')
        self.assertRaises(TypeError, Matrix, [1, 2, 3])
        self.assertRaises(TypeError, Matrix, [[1, 2, 3], [1, 2]])

        a = [[1, 2],
             [2, 3]]
        try:
            Matrix(a)
        except Exception as e:
            self.fail('Matrix initialization is failed for {0}: {1}'.format(a, e))

    def test_add(self):
        a = [[1, 2],
             [2, 1]]
        b = [[0, -1],
             [1, 2]]
        c = [[1, 1],
             [3, 3]]
        self.assertEqual(Matrix(a) + Matrix(b), Matrix(c))
        self.assertEqual(Matrix(b) + Matrix(a), Matrix(c))

        d = [[0, -1],
             [1, 2],
             [0, 0]]

        with self.assertRaises(IndexError):
            Matrix(a) + Matrix(d)

    def test_add_negative(self):
        a = Matrix([[0, 0],
                    [0, 1]])
        with self.assertRaises(TypeError):
            a + 1
        with self.assertRaises(TypeError):
            a + [[0], [1]]
        with self.assertRaises(TypeError):
            a + 'sdfs'


    def test_mul_sq(self):
        a = Matrix([[1, 2], [2, 3]])
        b = Matrix([[1, 0], [0, 1]])

        self.assertEqual(a * b, a)
        self.assertEqual(b * b, b)

    def test_mul_no_sq(self):
        a = [[1, 2, 3],
             [-3, 2, 1]]
        b = [[1, 2],
             [-2, -1],
             [1, 0]]
        c1 = [[0, 0], [-6, -8]]
        c2 = [[-5, 6, 5], [1, -6, -7], [1, 2, 3]]
        self.assertEqual(Matrix(a) * Matrix(b), Matrix(c1))
        self.assertEqual(Matrix(b) * Matrix(a), Matrix(c2))

    def test_mul_no_sq_negative(self):
        a = [[1, 2, 3],
             [-3, 2, 1]]
        b = [[1, 2],
             [-2, -1],
             [1, 0],
             [0, 2]]
        with self.assertRaises(IndexError):
            Matrix(a) * Matrix(b)
        try:
            Matrix(b) * Matrix(a)
        except IndexError:
            self.fail('Index error on multiplying {0} on {1}'.format(b, a))

    def test_mul_int(self):
        a = [[2, 1, 3],
             [-1, 1, 0]]
        b = [[6, 3, 9],
             [-3, 3, 0]]
        self.assertEqual(Matrix(a) * 3, Matrix(b))
        self.assertEqual(3 * Matrix(a), Matrix(b))

    def test_mul_negative(self):
        a = Matrix([[1, 2], [2, 3]])

        with self.assertRaises(TypeError):
            a * [[1, 2]]
        with self.assertRaises(TypeError):
            a * 'test'

    def test_identity(self):
        identity_arr = [[0] * 5 for _ in xrange(5)]
        for i in xrange(len(identity_arr)):
            identity_arr[i][i] = 1
        self.assertEqual(Matrix.Identity(5), Matrix(identity_arr))

    def test_zeros(self):
        zeros_arr = [[0] * 5 for _ in xrange(7)]
        self.assertEqual(Matrix.Zeros(5, 7), Matrix(zeros_arr))


class TestQuickSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_len_1(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_len_2(self):
        self.assertEqual(quick_sort([2, 1]), [1, 2])

    def test_len_3(self):
        self.assertEqual(quick_sort([3, 2, 1]), [1, 2, 3])

    def test_len_4(self):
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_len_5(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort(self):
        for i in xrange(10):
            array = [random.randint(-1000, 1000) for _ in xrange(1500)]
            self.assertEqual(quick_sort(array), sorted(array))

    def test_time(self):
        array = [random.randint(-10000, 10000) for _ in xrange(15000)]
        start = time.time()
        quick_sort(array)
        end_time = time.time() - start
        self.assertTrue(end_time < 1)

if __name__ == '__main__':
    unittest.main()
