import re

log = 'July 31 my computer bad_process[12345]: ERROR performing package update'
regex = r'\[(\d+)]'
result = re.search(regex, log)
print(result)
print(type(result))
print(result.span)
print(result[1])
