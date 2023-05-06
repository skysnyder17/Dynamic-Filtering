import time

def filter_line(line, filter_func):
    """Filters a single line of text using a filter function."""
    if filter_func(line):
        return line
    else:
        return None

def filter_stream(stream, filter_func):
    """Filters a stream of text using a filter function."""
    for line in stream:
        filtered_line = filter_line(line, filter_func)
        if filtered_line:
            yield filtered_line

def load_filter(filter_filename):
    """Loads a filter function from a file."""
    with open(filter_filename, 'r') as f:
        filter_source = f.read()
    filter_func = compile(filter_source, filter_filename, 'eval')
    return lambda line: eval(filter_func, {'line': line})

if __name__ == '__main__':
    # Set up the initial filter function
    filter_filename = 'filter.txt'
    filter_func = load_filter(filter_filename)

    # Open the input stream
    input_filename = 'input.txt'
    input_stream = open(input_filename, 'r')

    # Filter the input stream
    for line in filter_stream(input_stream, filter_func):
        print(line.strip())

    # Monitor the filter file for changes and reload the filter function
    while True:
        time.sleep(1)
        try:
            new_filter_func = load_filter(filter_filename)
            if new_filter_func != filter_func:
                print('Reloading filter...')
                filter_func = new_filter_func
        except:
            pass
