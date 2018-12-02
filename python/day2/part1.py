import collections
import sys


strings_with_double = 0
strings_with_triple = 0

for line in sys.stdin:
    counter = collections.Counter(line.strip())
    if 2 in counter.values():
        strings_with_double += 1
    if 3 in counter.values():
        strings_with_triple += 1

print(
    f"Found {strings_with_double} and {strings_with_triple} for a product of "
    f"{strings_with_triple * strings_with_double}"
)
