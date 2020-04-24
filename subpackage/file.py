from os import sys, path


def f():
    print('Inside subpackage')


if __name__ == '__main__':
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import test_imports

    __package__ = 'test_imports.subpackage'

    from .. import file
    file.f()
    print('Success')
    f()
