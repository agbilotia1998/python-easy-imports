from os import sys, path


def f():
    print('Inside module')


if __name__ == '__main__':
    import test_imports

    __package__ = 'test_imports.subpackage'
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from .. import file
    file.f()
    print('Success')
    f()
