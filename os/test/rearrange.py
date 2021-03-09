import re

def rearrange_name(name):
    result = re.search(r'^([\w \.-]*), ([\w \.-]*)$', name)
    if result is None:
        return ''
    return '{} {}'.format(result[2], result[1])

# print(rearrange_name('Ikhsanudin, Arif'))
# print(rearrange_name('Lovelace, Ada'))
