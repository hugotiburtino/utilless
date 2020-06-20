def bind(iterable, binder, lastbinder):
    """
    # TODO add better description
    Takes a iterable and returns a string
    with all the items separated by binder parameter
    """
    # raises error if iterable is empty
    if not iterable:
        raise ValueError("The iterable is empty")

    # turns all items of iterable into strings
    words = list(map(str, iterable))

    # join words with binder until before the last one,
    # which is on its turn bound with the lastbinder. See commaand
    return binder.join(words[: len(words) - 1]) + lastbinder + words[-1]
