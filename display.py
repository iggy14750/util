
"""
Print a given iterable of elements which can be printed as strings,
print them all in a 2-dimensional table, not unlike hexdump.
"""
def table(iterable, columns=8):
    # Loop rows
    row = 0
    iterator = iter(iterable)
    while True:
        # Index of first item of this row
        print("{:04}\t".format(row*columns), end='')
        # Loop columns within a row
        for col in range(columns):
            try:
                elem = next(iterator)
                print("{}\t".format(elem), end='')
            except StopIteration:
                return
        print() # I just want to newline
        row += 1

