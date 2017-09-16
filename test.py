def s(i):
    print('zaczynam z liczbą', i)
    if i == 0:
        result = 1
    else:
        result = i * s(i - 1)
    print('kończę z liczbą', i)
    return result


def f(i):
    print('zaczynam z liczbą', i)
    if i in [0, 1]:
        result = 1
    else:
        result = f(i - 1) + f(i - 2)
    print('kończę z liczbą', i)
    return result


def h(n, source, target, helping):
    if n > 0:
        h(n - 1, source, helping, target)
        print('przenoszę klocek rozmiaru', n, 'z', source, 'na', target)
        h(n - 1, helping, target, source)


def sign(i):
    if i > 0:
        res = 1
    else:
        if i == 0:
            res = 0
        else:
            res = -1
    return res


def sign2(i):
    if i > 0:
        return 1
    if i == 0:
        return 0
    return -1


def mul(i, j):
    if j < 0:
        return -i + mul(i, j + 1)
    if j == 0:
        return 0
    if j == 1:
        return i
    else:
        return i + mul(i, j - 1)


def is_palindrom(text):
    if len(text) in [0, 1]:
        return True
    if text[0] == ' ':
        return is_palindrom(text[1:])
    if text[-1] == ' ':
        return is_palindrom(text[:-1])
    if text[0].lower() == text[-1].lower():
        return is_palindrom(text[1:-1])
    return False

print(is_palindrom('rAdar'))

# print(mul(2, -1))

# print(f(5))
