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


def isEqual(a, b):
    '''Determine if a == b '''
    return a == b


def generate_user_email(firstname, lastname, age):
    ''' Generate an email for the user '''
    return "{}{}_{}@racoondevs.com".format(firstname, lastname, age)
