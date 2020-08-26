# Number Display

Small Flask app that displays a list of numbers ranging from 1 to a number given in url and modified via paths.

## Basic Implementation

1. Given a url, generate list of all numbers from 1 to specified number in path.
2. If 'odd', 'even', or 'prime' are also in path, set filter functions to get such numbers from list.
3. Apply filters if any to list and pass it and other information to generic HTML template for rendering.