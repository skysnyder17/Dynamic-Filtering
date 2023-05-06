import os

def get_input(prompt):
    """Gets user input from the command line."""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print('\n')
        return ''

def edit_filter(filter_filename):
    """Opens the filter file in an editor."""
    editor = os.environ.get('EDITOR', 'nano')
    os.system('{} {}'.format(editor, filter_filename))

if __name__ == '__main__':
    # Set up the filter filename
    filter_filename = 'filter.txt'

    # Loop to allow the user to modify the filter expression
    while True:
        # Prompt the user to edit the filter file
        input_string = get_input('Press enter to edit the filter expression, or "q" to quit: ')
        if input_string.lower() == 'q':
            break

        # Open the filter file in an editor
        edit_filter(filter_filename)

        # Print a confirmation message
        print('Filter expression updated. Press enter to continue.')
        input()
