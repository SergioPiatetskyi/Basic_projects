import random

#                "Password generator"

# maximum quantity of elements in password, can be changed
MAXIMUM_LENGTH = 10

#        arrays of characters for password

# 1) digit`s list
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2) lower register of letter`s list
lower_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 3) upper register of letter`s list
upper_let = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 4) special sign`s list for password
spec_signs = ['@', '#', '$', '%', '=',
              ':', '?', '.', '/', '|',
              '~', '>', '*', '(', ')']

# combining of all sets from above by 'concatenating' 1) + 2) + 3) + 4)
COMBINED_lists = digits + lower_let + upper_let + spec_signs


# "pulling out" one random element from EACH list of characters
# here the password has -4- elements only
# 1)
random_digits = random.choice(digits)
# 2)
random_lower_let = random.choice(lower_let)
# 3)
random_upper_let = random.choice(upper_let)
# 4)
random_spec_signs = random.choice(spec_signs)


# combining of above randomly "pulled out" elements
COMBINED_random = random_digits + random_lower_let +\
                  random_upper_let + random_spec_signs

for x in range(MAXIMUM_LENGTH):
    COMBINED_random = COMBINED_random + random.choice(COMBINED_lists)

password = ''
for x in COMBINED_random:
    password = password + x

print(password)
