import string
import sys

case_flip_mapping = dict(zip(string.ascii_lowercase, string.ascii_uppercase))
case_flip_mapping.update(
    dict(zip(string.ascii_uppercase, string.ascii_lowercase)))

input_string = sys.stdin.readline().strip()

result_string = []

for char in input_string:
    if not result_string:  # Case when the string is empty
        result_string.append(char)
        continue
    elif char == case_flip_mapping[result_string[-1]]:
        result_string.pop()
    else:
        result_string.append(char)

print("".join(result_string))
print(len("".join(result_string)))
