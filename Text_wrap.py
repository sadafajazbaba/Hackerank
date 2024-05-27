import textwrap
def wrap(string, max_width):
    string = string
    max_width = max_width
    wrapped = textwrap.fill(string,max_width)
    return wrapped