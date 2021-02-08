"""
a{b,c}d returns abd acd
"""
import itertools


def bash_convert(s):
    """
    :param s: str, input string, containing {} and other chars
    :return: spaced strings
    """
    # First, adding the square brackets like in lists and replacing curly ones too
    # Putting commas as well to make this string look like a list
    s = "['" + s.replace("{", "','").replace("}", "','") + "']"
    # eval() "executes" the code in the string and makes it the actual list
    input_list = eval(s)
    # Now we have a list looking like this: ['a', 'd,b', 'n']. Need to split the items separated by comma
    input_list = [list(item.split(",")) for item in input_list]
    # Now we have list of lists: [['a'], ['d', 'b'], ['n']]
    # Sequentially multiply all the lists, starting with the first two: input_list[0] and input_list[1] –
    # ['a'] and ['d', 'b']: itertools.product(['a'], ['d', 'b']) = [('a', 'd'), ('a', 'b')]
    # ''.join() will squeeze tuples into strings: ['ad', 'ab']
    res = [''.join(pair) for pair in itertools.product(input_list[0], input_list[1])]
    # Sequentially adding all the rest of the items to the product:
    for i in range(2, len(input_list)):
        res = [''.join(pair) for pair in itertools.product(res, input_list[i])]
    # Print result list items
    return " ".join(res)


if __name__ == "__main__":
    print(bash_convert("a{d,b}n"))
    print(bash_convert("a{d{8,7}}n"))
    print(bash_convert("{d{8,7,9}}uun"))
