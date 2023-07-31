from calculator import square

def main():
    test_square
def test_square():
        assert square(2) == 4
    except AssertionError:
        print('error')
    try:
        assert square(3) == 9
    except AssertionError:
        print('error')
if __name__ == '__main__':

    main()