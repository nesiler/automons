def print_line(char, length=50):
    print(char * length)


def line_summary():
    print_line('#')


def line_info():
    print_line('*')


def line_warning():
    print_line('-')


def line_error():
    print_line('!')


def line_success():
    print_line('=')


def line_input():
    print_line('>')


def line_generate():
    print_line('+')
