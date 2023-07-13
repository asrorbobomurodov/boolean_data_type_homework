def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a**(1/2)%1==0
print(main(121))
print(main(30))