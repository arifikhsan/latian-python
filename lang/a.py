filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
    name, ext = filename.split('.')
    if ext == 'hpp':
        newfilenames.append('{}.{}'.format(name, 'h'))
    else:
        newfilenames.append('{}.{}'.format(name, ext))

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    say = []
    words = text.split()
    for word in words:
        w = ''
        first = word[0]
        w = word[1:] + first + 'ay'
        # print(w)
        say.append(w)
        # Create the pig latin word and add it to the list
        # Turn the list back into a phrase
    return ' '.join(say)
#   return w


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))

immutable

def group_list(group, users):
  members = ', '.join(users)
  return '{}: {}'.format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


def guest_list(guests):
	for guest in guests:
		print('{} is {} years old and works as {}'.format(guest[0], guest[1], guest[2]))
		# for name, age, job in guest:

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
