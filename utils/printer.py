def print_line(char, length=50):
    print(char * length)


def line_error(l=50):
    print_line('!', l)


def error_message(message, l=50):
    line_error(l)
    print(message)
    line_error(l)
