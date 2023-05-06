
# Dynamic Filter Scripts

These Python scripts allow you to filter a stream of logs or text lines using a dynamic filter expression that can be modified on-the-fly. The scripts include:

- `dynamic_filter.py`: The main script that reads a stream of input and filters it using a dynamic filter function that can be reloaded when the filter expression changes.
- `edit_filter.py`: A supporting script that allows you to edit the filter expression in a text editor.

## How to Use These Scripts

To use these scripts, follow these steps:

1. Create a file called `input.txt` and add some sample log lines or text lines to it.

2. Create a file called `filter.txt` and add an initial filter expression to it. This filter expression should be a Python expression that evaluates to `True` or `False` based on whether a given line should be filtered or not. For example, you could use the following filter expression to match any lines that contain the string "ERROR":

   ```
   'ERROR' in line
   ```

   Note that the filter expression must reference a variable called `line` in order to filter each line of text.

3. Run the `dynamic_filter.py` script using the command `python dynamic_filter.py`.

4. The script will read the input stream from `input.txt` and filter it using the filter expression in `filter.txt`. Only lines that match the filter expression will be printed to the console.

5. To modify the filter expression, open `filter.txt` in a text editor and edit the filter expression. For example, you could modify the filter expression to match any lines that contain the string "WARNING":

   ```
   'WARNING' in line
   ```

6. Save the changes to `filter.txt`. The `dynamic_filter.py` script will detect the changes and automatically reload the filter expression. The filtered output will now include lines that match the new filter expression.

7. To exit the script, press `Ctrl+C`.

Additionally, you can use the `edit_filter.py` script to edit the filter expression in a text editor. This is a more convenient way to modify the filter expression than manually editing `filter.txt`. To use this script, simply run `python edit_filter.py` and follow the prompts. The script will open `filter.txt` in the default text editor (or the editor specified by the `EDITOR` environment variable). After you've made your changes and saved the file, return to the command line and press enter to confirm the changes.

## Requirements

These scripts were written for Python 3. No additional dependencies are required.
