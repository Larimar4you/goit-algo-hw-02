"""
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.
"""

from collections import deque


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


test_strings = ["Друже!", "Я в захватi вiд завдання!", "404"]

for s in test_strings:
    if is_palindrome(s):
        print(f'"{s}" -> Паліндром')
    else:
        print(f'"{s}" -> Не паліндром')
