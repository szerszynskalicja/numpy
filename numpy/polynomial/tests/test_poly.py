import numpy as np
import sys
import numpy.polynomial.polynomial as poly
from numpy.testing import (
        assert_almost_equal, assert_raises, assert_equal, assert_,
        assert_warns, assert_array_equal, assert_raises_regex)


class TestPolysub:

    def test_polysub_int(self):
        #arrange
        c1 = [2, 3, 4]
        c2 = [3, 4, 5]
        #act
        result = poly.polysub(c1, c2)
        #assert
        assert_equal(result, [-1, -1, -1])

    def test_polysub_float(self):
        #arrange 
        c1 = [2.0, 3.0, 4.0]
        c2 = [3.0, 4.0, 5.0]
        #act
        result = poly.polysub(c1, c2)
        #assert
        assert_equal(result, [-1.0, -1.0, -1.0])

    def test_polysub_float_2(self):
        #arrange 
        c1 = [5.8, 100.3, 200.5]
        c2 = [3.0, -4.0, 5.0]
        #act
        result = poly.polysub(c1, c2)
        #assert
        assert_equal(result, [2.8, 104.3, 195.5])

    def test_polysub_int_ne(self):
        #arrange 
        c1 = [sys.maxsize, 500, 21, 302]
        c2 = [sys.maxsize, -4, 5]
        #act
        result = poly.polysub(c1, c2)
        #assert
        assert_equal(result, [0, 504, 16, 302])

    def test_polysub_float_ne(self):
        #arrange 
        c1 = [165.55, 118.33, 200.5, 300.5]
        c2 = [0.55, -4.33, 5.0]
        #act
        result = poly.polysub(c1, c2)
        #assert
        assert_equal(result, [165.0, 122.66, 195.5, 300.5])

    def test_polysub_tozero(self):
        #arrange
        c1 = [233.33, 345.44, 4.33]
        c2 = [233.33, 345.44, 4.33]
        #act
        result = poly.polysub(c1, c2)
        #assert 
        assert_equal(result, [0.])

    