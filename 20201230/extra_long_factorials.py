"""
hackerrank.com/challenges/extra-long-factorials
"""
#!/bin/python3
import os


# Complete the extraLongFactorials function below.
def naiveExtraLongFactorials(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res


def extraLongFactorials(n):
    n = int(n)
    d = [1]
    for i in range(2, n + 1):
        for j in range(len(d)):
            d[j] *= i
        for j in range(len(d)):
            if d[j] < 10:
                continue
            if j == len(d) - 1:
                d.append(0)
            d[j + 1] += d[j] // 10
            d[j] %= 10
    return ''.join(reversed([str(i) for i in d]))


if __name__ == '__main__':
    inputs_path = "extra-long-factorials-testcases/input"
    outputs_path = "extra-long-factorials-testcases/output"
    inputs = os.listdir(inputs_path)
    outputs = os.listdir(outputs_path)
    for inpt, outpt in zip(inputs, outputs):
        inpt = open(os.path.join(inputs_path, inpt)).read()
        outpt = open(os.path.join(outputs_path, outpt)).read()
        assert extraLongFactorials(inpt) == outpt



