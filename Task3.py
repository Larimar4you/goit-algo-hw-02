from collections import deque
import string


def is_antipolindrome(s):
    s = "".join(c for c in s if c.isalnum()).lower()
    d = deque(s)

    if len(d) <= 1:
        return False

    while len(d) > 1:
        if d.popleft() == d.pop():
            return False
        return True


test_strings = ["Радар", "Привіт", "сусiд"]

for s in test_strings:
    if is_antipolindrome(s):
        print(f'"{s}" -> антипаліндром')
    else:
        print(f'"{s}" -> паліндром')
