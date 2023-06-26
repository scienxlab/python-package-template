from mypackage import myfunction


EPSILON = 1e-9

def test_myfunction():
    """
    Test that our roots are square.
    """
    assert abs(myfunction(1000) - 31.6227766017) < EPSILON
