def aggregate(args):
    ''' Get the total of a list '''
    total = 0
    for item in args:
        total += item
    return total


def check_existence(item, args):
    '''Check if item exists in list '''
    if item in args:
        return True
