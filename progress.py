def print_progress_bar(iter: int, total: int, width: int) -> None:
    iter += 1
    percentage = "{0:.2f}%".format(iter / total * 100)
    fill_width = int(width * iter / total)
    bar = '#' * fill_width + '-' * (width - fill_width)
    print(f"\rProgress: {percentage} [{bar}]", end="")