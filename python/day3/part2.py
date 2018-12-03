import re
import sys
from dataclasses import dataclass


@dataclass
class ClaimInfo:
    claim_number: int
    x: int
    y: int
    width: int
    height: int


def build_initial_square(width=1000, height=1000):
    square = []
    for _ in range(width):
        row = [0 for _ in range(height)]
        square.append(row)
    return square


def parse_input_into_claims():
    line_regex = re.compile(
        r"#(?P<CLAIMANT>\d+) @ (?P<X>\d+),(?P<Y>\d+): "
        r"(?P<WIDTH>\d+)x(?P<HEIGHT>\d+)"
    )

    claim_info = []
    for line in sys.stdin:
        line = line.strip()

        match = line_regex.match(line)
        if not match:
            raise RuntimeError(f"Line did not match: {line}")

        claim_number = int(match.group("CLAIMANT"))
        x = int(match.group("X"))
        y = int(match.group("Y"))
        width = int(match.group("WIDTH"))
        height = int(match.group("HEIGHT"))

        claim_info.append(
            ClaimInfo(
                claim_number=claim_number,
                x=x,
                y=y,
                width=width,
                height=height
            )
        )
    return claim_info


square = build_initial_square()
claim_info = parse_input_into_claims()

for claim in claim_info:
    for x_position in range(claim.x, claim.x + claim.width):
        for y_position in range(claim.y, claim.y + claim.height):
            square[x_position][y_position] += 1


def is_valid_claim(square, claim):
    for x_position in range(claim.x, claim.x + claim.width):
        for y_position in range(claim.y, claim.y + claim.height):
            if square[x_position][y_position] > 1:
                return False
    return True


for claim in claim_info:
    if is_valid_claim(square, claim):
        print(f"Valid claim is #{claim.claim_number}")
        break
