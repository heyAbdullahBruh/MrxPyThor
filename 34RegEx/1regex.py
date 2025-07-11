#🔍 Regex (Regular Expressions) in Python is a powerful tool used to search, match, extract, or replace patterns in text — like emails, phone numbers, words, or formats.

# In Python, regex is handled by the re module.

'''
| Pattern | Meaning                       | Example Match        |       |               |
| ------- | ----------------------------- | -------------------- | ----- | ------------- |
| `.`     | Any character except newline  | `a.c` → "abc", "axc" |       |               |
| `^`     | Start of string               | `^Hi` → "Hi there"   |       |               |
| `$`     | End of string                 | `end$` → "the end"   |       |               |
| `\d`    | Digit (0–9)                   | `\d\d` → "99"        |       |               |
| `\w`    | Word char (a–z, A–Z, 0–9, \_) | `\w+` → "Hello\_123" |       |               |
| `\s`    | Whitespace                    | `\s` → space, tab    |       |               |
| `*`     | 0 or more repetitions         | `a*` → "", "aaa"     |       |               |
| `+`     | 1 or more repetitions         | `a+` → "a", "aa"     |       |               |
| `?`     | 0 or 1 (optional)             | `a?` → "", "a"       |       |               |
| `[]`    | Match any character inside    | `[aeiou]` → "a", "e" |       |               |
| \`      | \`                            | OR operator          | \`cat | dog\` → "cat" |
| `()`    | Grouping                      | `(abc)+` → "abcabc"  |       |               |

'''