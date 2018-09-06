def bold(fn):
    print('4')

    def inner():
        print('1')
        return ('<b>' + fn() + '</b>')
    return inner


def italic(fn):
    def inner():
        print('2')
        return ('<i>' + fn() + '</i>')
    return inner


@bold
@italic
def test():
    print('3')
    return 'Hello'


ret = test()
print(ret)
