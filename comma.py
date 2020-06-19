# comma.py

def justcomma(iterable):
    """
    Function that takes a iterable and returns a string 
    with all the items separated by a comma and a space, 
    with and inserted before the last item. 
    """
    # raises error if iterable is empty
    if not iterable:
        raise ValueError('The iterable is empty')

    # turn all items of iterable into strings
    string_list = list(map(str, iterable))
    
    return ','.join(string_list)

def commaspace(iterable):
    """
    Function that takes a iterable and returns a string 
    with all the items separated by a comma and a space.
    """

    # raises error if iterable is empty
    if not iterable:
        raise ValueError('The iterable is empty')

    # turn all items of iterable into strings
    string_list = list(map(str, iterable))
    
    return ', '.join(string_list)


