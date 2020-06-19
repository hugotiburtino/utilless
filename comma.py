# comma.py

def commator(iterable, binder=',', lastbinder=','):
    """
    Mother of other functions like justcomma and commaspace.
    Takes a iterable and returns a string 
    with all the items separated by binder parameter
    """
    # raises error if iterable is empty
    if not iterable:
        raise ValueError('The iterable is empty')

    # turns all items of iterable into strings
    words = list(map(str, iterable))
    
    return binder.join(words[:len(words) - 1]) + lastbinder + words[-1]

def justcomma(iterable):
    """
    Function that takes a iterable and returns a string 
    with all the items separated by a comma 
    """
    return commator(iterable)

def commaspace(iterable):
    """
    Function that takes a iterable and returns a string 
    with all the items separated by a comma and a space.
    """
    return commator(iterable, ', ', ', ')

def commaand(iterable):
    """
    Function that takes a iterable and returns a string 
    with all the items separated by a comma and a space, 
    with and inserted before the last item. 
    """
    return commator(iterable, ', ', ', and ')
