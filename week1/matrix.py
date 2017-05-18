class Matrix(object):
    def __new__(cls, *args):
        if len(args) > 1:
            raise TypeError()
        mx = args[0]
        if not isinstance(mx, list):
            raise TypeError("'{0}' is not a matrix".format(mx))
        if not all(map(lambda x: isinstance(x, list) and len(x) == len(mx[0]), mx)):
            raise TypeError("'{0}' is not a matrix".format(mx))
        return super(Matrix, cls).__new__(cls)

    @classmethod
    def Zeros(cls, x, y):
        return cls([[0] * x for _ in xrange(y)])

    @classmethod
    def Identity(cls, x):
        matrix = [[0] * x for _ in xrange(x)]
        for i in xrange(x):
            matrix[i][i] = 1
        return cls(matrix)

    def __init__(self, matrix):
        self._matrix = matrix

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix([[x * other for x in line] for line in self])
        elif isinstance(other, self.__class__):
            if len(self._matrix[0]) != len(other):
                raise IndexError('cannot multiply Matrixes of {0}x{1} and {2}x{3} sizes'.format(
                    len(self._matrix), len(self._matrix[0]), len(other), len(other[0])))
            new_matrix = [[sum(self._matrix[i][r] * other[r][j] for r in xrange(len(other)))
                           for j in xrange(len(other[0]))]
                          for i in xrange(len(self))]
            return Matrix(new_matrix)
        else:
            raise TypeError("cannot multiply 'Matrix' and '{0}'".format(other.__class__))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for i in xrange(len(self)):
            for j in xrange(len(self[0])):
                if self._matrix[i][j] != other[i][j]:
                    return False
        return True

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("cannot concantenate 'Matrix' and '{0}'".format(other.__class__))
        if len(other) != len(self) or len(self[0]) != len(other):
            raise IndexError('cannot concantenate Matrixes of {0}x{1} and {2}x{3} sizes'.format(
                len(self._matrix), len(self._matrix[0]), len(other), len(other[0])))
        new_matrix = [[a + b for a, b in zip(line_a, line_b)]
                      for line_a, line_b in zip(self, other)]
        return Matrix(new_matrix)

    def __len__(self):
        return len(self._matrix)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError
        if item >= len(self._matrix):
            raise IndexError
        return self._matrix[item]
