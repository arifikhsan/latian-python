import re

# result = re.match(r'([#+])', '### Start of program')
result = re.sub(r'(#+)', '//', '### Start of program')
print(result)
# print(result.groups())

