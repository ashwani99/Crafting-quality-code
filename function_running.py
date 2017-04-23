def function_runner(f):
    """ (function) -> NoneType
    
    A function runner. Call f.
    """

    f()

def function_1():
    """ () -> NoneType
        
    Print that this function was called.
    """

    print('Function_1 was called')


def function_2():
    """ () -> NoneType

    Print that this function was called.
    """

    print('Function_2 was called')

if __name__ == '__main__':
    function_runner(function_2
                    )