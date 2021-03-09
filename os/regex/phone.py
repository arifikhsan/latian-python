import re

# result = re.sub('^\d{3}-\d{3}-\d{4}', '(\1) \2-\3', '212-345-9999')
result = re.sub(r'(\d{3})-(\d{3})-(\d{4})', r'(\1) \2-\3', '212-345-9999')
print(result)
# print(result.groups())
# print(result[1])

# result = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')
# print(result.groups())

