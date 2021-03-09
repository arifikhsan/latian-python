import re

log = 'July 31 my computer bad_process[12345]: ERROR performing package update'
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])

result = re.search(regex, 'A completely different string that also has nmbers [34567]')
print(result[1])

result = re.search(regex, '99 elephants in a [cage]')
# print(result[1])

def extract_pid(long_line):
    regex = r'\[(\d+)\]'
    result = re.search(regex, long_line)
    if result is None:
        return ''
    return result[1]

print(extract_pid(log))
print(extract_pid('99 elephants in a [cage]'))
