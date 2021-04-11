import random


def make_code(n):
    res = ''
    for i in range(n):
        s1 = chr(random.randint(65, 90))  # chr() 返回一个字符相对应的Unicode字符
        s2 = str(random.randint(0, 9))
        res += random.choice([s1, s2])
    return res


print(make_code(6))
