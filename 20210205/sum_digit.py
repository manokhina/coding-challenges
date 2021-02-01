#!/bin/python3


# Complete the superDigit function below.
def _superDigit(n, k):
    """passes 8/12"""
    n *= k
    while len(str(n)) > 1:
        n = sum([superDigit(int(char), 1) for char in str(n)])
    return n


def superDigit(n, k):
    """passes 12/12"""
    while len(str(n)) > 1:
        n = sum([superDigit(int(char), 1) for char in str(n)])
    return sum([int(char) for char in str(n*k)])


if __name__ == '__main__':
    print(superDigit("456", 3))
    print(superDigit("9875", 4))
    print(superDigit("148", 3))
    print(superDigit("123", 3))

