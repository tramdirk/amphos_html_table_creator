# ah yes, the negotiator


def negotiate():
    print('\nWelcome, in the following steps we will create a template for your HTML-table.')
    print('Made by Moritz Moeckel\n')
    headline = input('what is the headline of your table?')
    subtitle = input('need a subtitle? leave empty if you dont')
    columns = input('how many columns do you need?')
    lines = input('how many lines do you need?(excluding table head)')

    i = 1
    titles = list()
    while i <= int(columns):
        titles.append(input('what is column ' + str(i) + ' called?'))
        i = i + 1

    to_return = dict()
    to_return['headline'] = headline
    to_return['subtitle'] = subtitle
    to_return['columns'] = columns
    to_return['lines'] = lines
    to_return['column_titles'] = titles

    return to_return
