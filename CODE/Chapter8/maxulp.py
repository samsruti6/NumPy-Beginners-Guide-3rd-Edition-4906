from __future__ import print_function
import numpy as np

eps = np.finfo(float).eps
print("EPS", eps)
print("1", np.testing.assert_array_max_ulp(1.0, 1.0 + eps))
print("2", np.testing.assert_array_max_ulp(1.0, 1 + 2 * eps, maxulp=2))
