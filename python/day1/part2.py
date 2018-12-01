import itertools
import sys


def main():
    input_list = [int(line.strip()) for line in sys.stdin]

    current_frequency = 0
    frequencies_seen = {0}

    for cycle_num, frequency in enumerate(itertools.cycle(input_list), 1):
        current_frequency += frequency
        if current_frequency in frequencies_seen:
            print(
                f"Saw frequency {current_frequency} twice on cycle {cycle_num}"
            )
            break
        else:
            frequencies_seen.add(current_frequency)


if __name__ == "__main__":
    main()
