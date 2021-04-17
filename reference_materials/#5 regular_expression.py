"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
{3, }   - Minimum number of times
{, 3}   - Maximum number of times

#### Sample Regexs ####
[A-Za-z0-9] 
"""
#%%
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
davemartin@bogusemail.com
michaelarnold@bogusemail.edu
johndavis@bogusemail.net
kurtwilson@bogusemail.com
stevedoe@bogusemail.com
nicoletaylor@bogusemail.com
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#%%
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.findall(text_to_search) # findall method return a list
print(matches)

#%%
matches = pattern.finditer(text_to_search) # finditer method return an iterator of Match obj
for match in matches:
    print(match)
# %%
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match.group()) # group method return the actual match values
#%%
pattern = re.compile(r'[89]00.\d\d\d.\d\d\d\d')
matches = pattern.findall(text_to_search)
print(matches)
# %%
pattern = re.compile(r'.+@.+\.')
matches = pattern.findall(text_to_search)
print(matches)
# %%
email_pattern1 = re.compile(r'https?://w?w?w?\.?.+\..+')
matches = email_pattern1.findall(text_to_search)
print(matches)
