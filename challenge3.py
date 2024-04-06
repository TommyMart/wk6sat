# palindrome

# string reversed is also the same as the original string

# firetruck = kcurterif -> not palindrome
# racecar = racecar -> palindrome

original_string = "racecar"

reversed_string = ""

for character in original_string: # f, i, r, e
    reversed_string = character + reversed_string # f, if, rif, erif...

print(reversed_string)

if (reversed_string == original_string):
    print("Is a palindrome")
else:
    print("Is not a palindrome")

name = "simon"
reverse_name = name[::-1]
print(reverse_name)