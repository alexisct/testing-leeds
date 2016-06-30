from mean import *

# this tests that the code works with integers ok
def test_ints():
    num_list = [1,2,3,4,5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

# this tests that the code works with zeros in the input ok
def test_zero():
    num_list=[0,2,4,6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

# this tests that the code works with non-integers ok
def test_double():
    # This one will fail in Python 2
    num_list=[1,2,3,4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp

# this tests that the code deals with large numbers ok
def test_long():
    big = 100000000
    obs = mean(range(1,big))
    exp = big/2.0
    assert obs == exp

