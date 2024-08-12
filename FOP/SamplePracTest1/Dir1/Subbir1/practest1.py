#
# Student Name: Abdur rahman kazi
# Student ID: 22402293
#
# practicetest1.py: Read in a string and print it
#
instring = input('Enter a string... ')
print("This string is : ", instring)


newString = instring.lower()

check = 0
matching = 0
position = 0

dup_rep_star = list(newString)
while(check < len(dup_rep_star)):
    if(newString[position] == newString[check]):
        matching += 1
        if(matching > 1):
            dup_rep_star[check] = '*'
            print("find replace word ", newString[check])
    if check == len(newString) -1:
        check = 1
        matching = 0
        position +=1
    else:
        check +=1
    if position == len(newString) -1:
        break  
print("String is ", "".join(dup_rep_star))

# Converting to array
string_upper_lower = list(instring)
for string in range(len(string_upper_lower)):
    letter = ""+ string_upper_lower[string]
    if letter.islower():
        string_upper_lower[string] = string_upper_lower[string].upper()
    else:
        string_upper_lower[string] = string_upper_lower[string].lower()

# convert to string
print("Check upper lower is ", "".join(string_upper_lower))


for star in range(len(dup_rep_star)):
    if dup_rep_star[star] == "*":
        string_upper_lower[star] = "*"

print("Final result is ", "".join(string_upper_lower))

