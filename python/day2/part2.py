import sys

input_list = [line.strip() for line in sys.stdin]
longest_string = max(len(s) for s in input_list)

# Idea is to remove one character at a time from EVERY string and then find
# which one is present twice.
for index_to_remove in range(longest_string):
    strings_seen = set()
    for string in input_list:
        string_with_character_removed = (
            f"{string[:index_to_remove]}{string[1 + index_to_remove:]}")
        if string_with_character_removed in strings_seen:
            print(f"Common characters: {string_with_character_removed}")
        else:
            strings_seen.add(string_with_character_removed)
