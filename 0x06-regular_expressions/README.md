Welcome to my 0x06-regular_expressions directory
By: Mohamed Amine Abahmane


Regular expressions (regex) are a powerful tool for pattern matching and manipulating text. Here are some common expressions and syntax used in regex:

Literal Characters:

Letters and digits: Matches the specified letter or digit as is. For example, a matches the letter "a", and 5 matches the digit 5.
Special characters: Some characters have special meanings in regex, such as ., *, +, ?, [, ], (, ), {, }, |, \, etc. To match these characters literally, you need to escape them using a backslash \.
Character Classes:

[ ]: Matches any single character within the brackets. For example, [aeiou] matches any vowel.
[^ ]: Matches any single character not within the brackets. For example, [^0-9] matches any non-digit character.
-: Represents a range of characters within brackets. For example, [a-z] matches any lowercase letter.
Metacharacters:

.: Matches any character except a newline character.
*: Matches zero or more occurrences of the preceding character or group.
+: Matches one or more occurrences of the preceding character or group.
?: Matches zero or one occurrence of the preceding character or group.
{n}: Matches exactly n occurrences of the preceding character or group.
{n,}: Matches n or more occurrences of the preceding character or group.
{n,m}: Matches between n and m occurrences of the preceding character or group.
|: Acts as an OR operator. Matches either the expression before or after the pipe.
^: Matches the beginning of a line or string.
$: Matches the end of a line or string.
Escape Sequences:

\d: Matches any digit character. Equivalent to [0-9].
\D: Matches any non-digit character. Equivalent to [^0-9].
\w: Matches any word character (alphanumeric and underscore). Equivalent to [a-zA-Z0-9_].
\W: Matches any non-word character (non-alphanumeric or non-underscore). Equivalent to [^a-zA-Z0-9_].
\s: Matches any whitespace character.
\S: Matches any non-whitespace character.
\b: Matches a word boundary.
\B: Matches a non-word boundary.
Grouping and Capturing:

( ): Groups characters together. For example, (ab)+ matches one or more occurrences of "ab".
(?: ): Non-capturing group. It groups the expression but does not capture the match.
These are just the basics of regular expressions. There are more advanced features and expressions available, depending on the specific regex implementation you're using. Regular expressions can be quite complex, but they offer a powerful way to search, validate, and manipulate text based on patterns.