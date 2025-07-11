# Meta characters ---> 


# 1. Basic Meta Characters--->

# | Meta | Meaning                      | Example     | Matches                        |
# | ---- | ---------------------------- | ----------- | ------------------------------ |
# | `.`  | Any character except newline | `a.c`       | `abc`, `a-c`, `a7c`            |
# | `^`  | Start of string              | `^Hi`       | `Hi there`, not `Say Hi`       |
# | `$`  | End of string                | `end$`      | `the end`, not `end now`       |
# | `*`  | 0 or more repetitions        | `go*gle`    | `ggle`, `gogle`, `gooogle`     |
# | `+`  | 1 or more repetitions        | `go+gle`    | `gogle`, `gooogle`, not `ggle` |
# | `?`  | 0 or 1 repetition            | `colou?r`   | `color`, `colour`              |
# |  `   |  `                           | OR operator |  `cat                          |
# | `()` | Group expressions            | `(ha)+`     | `ha`, `hahaha`                 |
# | `[]` | Character class (1 from set) | `[aeiou]`   | any vowel                      |
# | `\`  | Escape special characters    | `\.`        | `.`                            |
# | `-`  | Range of characters          | `[a-z]`     | `a` to `z`                     |
# | `[^ ]`  | Negation (when first in `[]`)| `[^0-9]`    | Any non-digit               |

# 2. Character Classes (Shortcuts)--->
# | Meta | Meaning                     | Matches                    |
# | ---- | --------------------------- | -------------------------- |
# | `\d` | Any digit                   | `0-9`                      |
# | `\D` | Any non-digit               | `a`, `#`, ` `              |
# | `\w` | Word char (letter/digit/\_) | `a-zA-Z0-9_`               |
# | `\W` | Non-word char               | `#`, `@`, space            |
# | `\s` | Whitespace                  | `space`, `\t`, `\n`        |
# | `\S` | Non-whitespace              | `a`, `1`, `@`              |
# | `\b` | Word boundary               | `\bword\b` → only `word`   |
# | `\B` | Not a word boundary         | `\Bword\B` → in `password` |

# 3. Quantifiers--->
# | Meta    | Meaning               | Example  | Matches             |
# | ------- | --------------------- | -------- | ------------------- |
# | `{n}`   | Exactly n times       | `a{3}`   | `aaa`               |
# | `{n,}`  | At least n times      | `a{2,}`  | `aa`, `aaa`, `aaaa` |
# | `{n,m}` | Between n and m times | `a{2,4}` | `aa`, `aaa`, `aaaa` |


import re 


# 1) . → Any character except newline
'''pattern = r".at"
text ="vat cat at nat -ay"
if re.match(pattern,text):
    print(re.findall(pattern,text)) #['vat', 'cat', ' at', 'nat']
else : 
    print('Not matched')'''

    
# 2) ^ → Start of string
'''pattern = r"^a"
text = 'ay Hello ! who are you ? \n I am a suii'
if re.match(pattern,text):
    print(re.findall(pattern,text)) #['a']
else : 
    print('Not matched')'''

# Create matchResult() universal funtion for check result--->
def matchResult(pattern,text) :
    if re.search(pattern,text):
        print(re.findall(pattern,text))
    else : 
        print('Not matched')

# 3) $ → End of string
'''pattern =r"siu$"
text= "Hello biuu!\n Who are you tiu? \n I dont know you siu"
matchResult(pattern,text)'''

#4) * → 0 or more repetitions
pattern =r"ap*le"
text= "apple aple apppple appppple"
matchResult(pattern,text) #['apple', 'aple', 'apppple', 'appppple']

#5) + → 1 or more repetitions
pattern =r"ap+le"
text= "apple alpe apppple appppple"
matchResult(pattern,text) #['apple', 'apppple', 'appppple']

# 6) ? → 0 or 1 repetition
pattern = r"colou?r"
text = "color colour colouur"
matchResult(pattern, text)  # ['color', 'colour']

# 7) | → OR operator
pattern = r"cat|dog"
text = "I have a cat and a dog but no bat."
matchResult(pattern, text)  # ['cat', 'dog']

# 8) () → Group expressions
pattern = r"(ha)+"
text = "haha hahahaha ha"
matchResult(pattern, text)  # ['ha', 'ha']

# 9) [] → Character class (1 from set)
pattern = r"[aeiou]"
text = "Regex is powerful"
matchResult(pattern, text)  # ['e', 'e', 'i', 'o', 'u']

#  10) \. → Escape special character .
pattern = r"\."
text = "Hello. How are you? Call me."
matchResult(pattern, text)  # ['.', '.']

# 11) - → Range of characters (inside [])
pattern = r"[a-z]"
text = "A1aB2bC3c"
matchResult(pattern, text)  # ['a', 'b', 'c']

# 12) [^] → Negation in character class
pattern = r"[^a-z]" # pattern = r"[^0-9]"
text = "abc123xyz456"
matchResult(pattern, text)  #['1', '2', '3', '4', '5', '6'] or ['a', 'b', 'c', 'x', 'y', 'z']

#13) \d → Digit 
pattern = r"\d"
text = "My number is 123456"
matchResult(pattern, text)  # ['1', '2', '3', '4', '5', '6']

# 14) \D → Non-digit
pattern = r"\D"
text = "123abc!@"
matchResult(pattern, text)  # ['a', 'b', 'c', '!', '@']

# \w → Word character (letters, digits, _)
pattern = r"\w"
text = "hello_123!"
matchResult(pattern, text)  # ['h', 'e', 'l', 'l', 'o', '_', '1', '2', '3']

# 16) \W → Non-word character
pattern = r"\W"
text = "hello@world!"
matchResult(pattern, text)  # ['@', '!']

# 17) \s → Whitespaces
pattern = r"\s"
text = "a b\tc\nd"
matchResult(pattern, text)  # [' ', '\t', '\n']

#  18) \S → Non-whitespace
pattern = r"\S"
text = "a b\tc\nd"
matchResult(pattern, text)  # ['a', 'b', 'c', 'd']

# 19) \b → Word boundary
pattern = r"\bcat\b"
text = "cat scatter cater cat!"
matchResult(pattern, text)  # ['cat', 'cat']

# ✅ 20) \B → Not a word boundary
pattern = r"\Bcat\B"
text = "scattering cater cat"
matchResult(pattern, text)  # ['cat']

#  21) {n} → Exactly n times
pattern = r"a{3}"
text = "a aa aaa aaaa"
matchResult(pattern, text)  # ['aaa', 'aaa']

# 22) {n,} → At least n times
pattern = r"a{2,}"
text = "a aa aaa aaaa"
matchResult(pattern, text)  # ['aa', 'aaa', 'aaaa']

# ✅ 23) {n,m} → Between n and m times
pattern = r"a{2,3}"
text = "a aa aaa aaaa"
matchResult(pattern, text)  # ['aa', 'aaa', 'aaa']

