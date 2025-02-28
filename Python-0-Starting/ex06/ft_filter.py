def ft_filter(func, iterable):
    """Return an iterator yielding\
        those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    items = []
    if func is None:
        return iterable
    for item in iterable:
        if func(item):
            items.append(item)
    return items
