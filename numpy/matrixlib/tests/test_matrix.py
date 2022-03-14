from numpy.matrixlib import matrix
from numpy.testing import (assert_equal)
import sys

class TestMatrixMean:

    def test_whole_matrix_mean_int(self):
        #arrange
        m = matrix([[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])
        #act
        result = m.mean()
        #assert
        assert_equal(result, 4.)

    def test_matrix_column_mean_int(self):
        #arrange
        m = matrix([[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])
        #act
        result = m.mean(0)
        #assert
        assert_equal(result, [[3., 4., 5.]])

    def test_matrix_row_mean_int(self):
        #arrange
        m = matrix([[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])
        #act
        result = m.mean(1)
        #assert
        assert_equal(result, [[1.],
                              [4.],
                              [7.]])

    def test_whole_matrix_mean_float(self):
        # arrange
        m = matrix([[0., 0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6, 0.7]])
        # act
        result = m.mean()
        # assert
        assert_equal(result, 0.35)

    def test_matrix_column_mean_float(self):
        # arrange
        m = matrix([[0., 0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6, 0.7]])
        # act
        result = m.mean(0)
        # assert
        assert_equal(result, [[0.2, 0.3, 0.4, 0.5]])

    def test_matrix_row_mean_float(self):
        # arrange
        m = matrix([[0.2, 0.4, 0.6, 0.8],
                    [0.4, 0.6, 0.8, 1.0]])
        # act
        result = m.mean(1)
        # assert
        assert_equal(result, [[0.5],
                              [0.7]])

    def test_whole_matrix_mean_to_zero(self):
        # arrange
        m = matrix([[-1, 1],
                    [1, -1]])
        # act
        result = m.mean()
        # assert
        assert_equal(result, 0)

    def test_matrix_column_mean_to_zero(self):
        # arrange
        m = matrix([[-1, 1],
                    [1, -1]])
        # act
        result = m.mean(0)
        # assert
        assert_equal(result, [[0., 0.]])

    def test_matrix_row_mean_float_to_zero(self):
        # arrange
        m = matrix([[-1, 1],
                    [1, -1]])
        # act
        result = m.mean(1)
        # assert
        assert_equal(result, [[0.],
                              [0.]])
