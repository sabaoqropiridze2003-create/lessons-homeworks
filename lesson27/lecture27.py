import re

text = "hello world"

result = re.search("hello", text)
print(result.group())  # Output: hello
