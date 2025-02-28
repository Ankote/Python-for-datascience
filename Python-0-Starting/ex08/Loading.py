
def ft_tqdm(lst: range):
    """Wraps an iterable and returns an iterator\
that displays a progress bar as the iterable is processed.
    """
    print("f")
    total = len(lst)  # Total number of iterations
    bar_length = 138

    for i, item in enumerate(lst, 1):  # Start counting from 1
        percentage = int(i / total) * 100
        filled_length = int(bar_length * i / total)
        bar = "\u2588" * filled_length + " " * (bar_length - filled_length - 1)
        print(f"\r{percentage}%|{bar}| {i}/{total}", end="", flush=True)
        yield item
