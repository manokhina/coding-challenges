"""
a{b,c}d returns abd acd
"""
import itertools


def bash_convert(s):
    """
    :param s: str, input string, containing {} and other chars
    :return: spaced strings
    """
    s = "['" + s.replace("{", "','").replace("}", "','") + "']"
    conv_s = eval(s)
    conv_s = [list(item.split(",")) for item in conv_s]
    res = [''.join(pair) for pair in itertools.product(conv_s[0], conv_s[1])]
    for i in range(2, len(conv_s)):
        res = [''.join(pair) for pair in itertools.product(res, conv_s[i])]
    return " ".join(res)


if __name__ == "__main__":
    print(bash_convert("a{d,b}n"))
    print(bash_convert("a{d{8,7}}n"))
    print(bash_convert("{d{8,7,9}}uun"))


