import re

# 1. Check if a string contains only a certain set of characters (a-z, A-Z, 0-9)
def check_string(s):
    pattern = '^[a-zA-Z0-9]+$'
    if re.match(pattern, s):
        print(f"'{s}' contains only a-z, A-Z, and 0-9.")
    else:
        print(f"'{s}' contains characters outside of a-z, A-Z, and 0-9.")

# 2. Matches a string that has an 'a' followed by zero or one 'b'
def match_a_followed_by_b(s):
    pattern = 'ab?'
    if re.search(pattern, s):
        print(f"'{s}' matches the pattern (a followed by zero or one 'b').")
    else:
        print(f"'{s}' does not match the pattern (a followed by zero or one 'b').")

# 3. Find sequences of lowercase letters joined by an underscore
def find_lowercase_underscore_sequence(s):
    pattern = '^[a-z]+(_[a-z]+)*$'
    if re.match(pattern, s):
        print(f"'{s}' matches the pattern of lowercase letters joined by underscores.")
    else:
        print(f"'{s}' does not match the pattern of lowercase letters joined by underscores.")

# 4. Matches a word containing 'z'
def contains_z(s):
    pattern = 'z'
    if re.search(pattern, s):
        print(f"'{s}' contains the letter 'z'.")
    else:
        print(f"'{s}' does not contain the letter 'z'.")

# Test the functions with different strings

# Test 1: Check string for allowed characters (a-z, A-Z, 0-9)
check_string("Hello123")  # Valid string
check_string("Hello@123")  # Invalid string

# Test 2: Matches 'a' followed by zero or one 'b'
match_a_followed_by_b("ab")   # Matches
match_a_followed_by_b("ac")   # Does not match

# Test 3: Find lowercase sequences joined by underscores
find_lowercase_underscore_sequence("hello_world")    # Valid
find_lowercase_underscore_sequence("hello123_world")  # Invalid (numbers)

# Test 4: Check if word contains 'z'
contains_z("amazing")  # Contains 'z'
contains_z("hello")   # Does not contain 'z'
