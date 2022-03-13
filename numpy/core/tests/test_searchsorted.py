import numpy as np
from numpy.testing import (assert_array_equal)


class TestSearchSorted:

    def test_left_obj(self):
        #arrange
        a = np.arange(5)
        v = np.array([0., 2., 4.], dtype = object)
        #act
        result = np.searchsorted(a,v, side="left") 
        #assert
        assert_array_equal(result, [0, 2, 4])
        
    def test_withNan_left_obj(self):
        #arrange
        a = np.arange(5)
        v = np.array([0., np.NaN, 2., np.NaN, 4.], dtype = object)
        #act
        result = np.searchsorted(a,v, side="left") 
        #assert
        assert_array_equal(result, [0, 0, 2, 0, 4])

    def test_withNan_right_obj(self):
        #arrange
        a = np.arange(5)
        v = np.array([0., np.NaN, 2., 3., -1.], dtype = object)
        #act
        result = np.searchsorted(a,v, side="right") 
        #assert
        assert_array_equal(result, [1, 5, 3, 4, 0])

    def test_withNan_right_float(self):
        #arrange
        a = np.arange(5)
        v = np.array([0., np.NaN, 2.0, 3., -1.0], dtype = float)
        #act
        result = np.searchsorted(a,v, side="right") 
        #assert
        assert_array_equal(result, [1, 5, 3, 4, 0])