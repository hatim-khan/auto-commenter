#Use Data Abstraction
def make_function_outline(name, args, return_type):

    return {
        'Name': name,
        'Arguments': args,
        'Return Type': return_type

    }



def get_name(function):
    return function['Name']
def get_args(function):
    return function['Arguments']
def get_return(function):
    return function['Return Type']

def form_arg_list(line):
    """ Get arg list from a line such as:
        ['def', 'find_closest(location,', 'centroids):']
    """
    args = line[1:] #get rid of def
    print(args[0])
    args[0] = args[0][args[0].index('(')+1: -1]
    args[-1] = args[-1][0:-2]
    return args

def write_function_to_file(file, function):
    #write name
    file.write('*********************************************')
    file.write('******', get_name(function), '******')
    file.write('*********************************************')

    #write arguments
    file.write('*', 'Arguments: ', get_args(function))
    file.write('*', 'Return: ', get_return(function))
