from my_lib import Stack


class BracketsException(Exception):
    pass


def check_for_brackets(string):
    brackets = Stack()
    pairs_by_open = {
        "(": ")",
        "<": ">",
        "{": "}",
        "[": "]",
    }
    pairs_by_close = {
        ")": "(",
        ">": "<",
        "}": "{",
        "]": "[",
    }
    i = 0
    for char in string:
        i += 1
        if char in pairs_by_open.keys():
            brackets.push(char)
        if char in pairs_by_close.keys():
            if brackets.is_empty():
                raise BracketsException("unexpected \"{}\"".format(char), i)
            need_in_stack = pairs_by_close[char]
            last_in_stack = brackets.top()
            if last_in_stack != need_in_stack:
                raise BracketsException("unexpected \"{}\", should be \"{}\"".format(char, pairs_by_open[last_in_stack]), i)
            if last_in_stack == need_in_stack:
                brackets.pop()
    if not brackets.is_empty():
        last_in_stack = brackets.top()
        raise BracketsException("unclosed \"{}\" in {} col".format(last_in_stack, i), i)


strs = [
    "kjash(klasn)<",
    "kjash(klasn)<>",
    "kja)sh(klasn)<}>",
    "kjash(klasn)><",
    "kjashklasn)>",
    "kjas(<hklasn)>",
]

for s in strs:
    e = "ok"
    try:
        check_for_brackets(s)
    except BracketsException as err:
        e = str(err.args[0])
        pos = int(err.args[1]) - 2
        print(s)
        print(" " * pos, "^-- error: ", e)
    else:
        print(s)
        print("-- ok --")
