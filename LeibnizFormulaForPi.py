def compute_pi(n):
    """
    Compute the value of pi using the first n terms of the Leibniz formula.
    """
    pi = 0
    sign = 1
    for i in range(n):
        pi += sign * 4 / (2 * i + 1)
        sign *= -1
    return pi

# Test the function with n = 10
print(compute_pi(10000))
