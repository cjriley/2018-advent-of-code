import string
import sys

case_flip_mapping = dict(zip(string.ascii_lowercase, string.ascii_uppercase))
case_flip_mapping.update(
    dict(zip(string.ascii_uppercase, string.ascii_lowercase)))
input_string = sys.stdin.readline().strip()


def react_string(input_string):
    result_string = []

    for char in input_string:
        if not result_string:  # Case when the string is empty
            result_string.append(char)
            continue
        elif char == case_flip_mapping[result_string[-1]]:
            result_string.pop()
        else:
            result_string.append(char)
    return "".join(result_string)


best_result = len(input_string)
best_letter = None
for lowercase_letter in string.ascii_lowercase:
    stripped_string = input_string.replace(
        lowercase_letter, ""
    ).replace(
        case_flip_mapping[lowercase_letter], ""
    )

    reacted = react_string(stripped_string)
    if len(reacted) < best_result:
        best_result = len(reacted)
        best_letter = lowercase_letter

print(
    f"Best result was of length [{best_result}] removing "
    f"{lowercase_letter}/{case_flip_mapping[lowercase_letter]}"
)
