#
#
#

instring = input('Enter a  string.... ')

print('Reversed string is : ', end="")
index = len(instring) - 1
while index > -1:
    print(instring[index], end="")
    index = index - 1
print()

# reversing
print('Reserved string is : ', end="")
for index in range(len(instring)-1, -1, -1):
    print(instring[index], end="")
print()

print('Reversed string is :', instring[::-1])
