import re
import sys


line_regex = re.compile(
    r"#(?P<CLAIMANT>\d+) @ (?P<X>\d+),(?P<Y>\d+): "
    r"(?P<WIDTH>\d+)x(?P<HEIGHT>\d+)"
)

square = []
for _ in range(1000):
    row = [0 for _ in range(1000)]
    square.append(row)


total_double_counted = 0

for line in sys.stdin:
    line = line.strip()

    match = line_regex.match(line)
    if not match:
        raise RuntimeError(f"Line did not match: {line}")

    x = int(match.group("X"))
    y = int(match.group("Y"))
    width = int(match.group("WIDTH"))
    height = int(match.group("HEIGHT"))

    for x_position in range(x, x + width):
        for y_position in range(y, y + height):
            square[x_position][y_position] += 1

            # Only count each square once (when it first becomes double
            # claimed)
            if square[x_position][y_position] == 2:
                total_double_counted += 1

print(f"Total double counted: {total_double_counted}")
