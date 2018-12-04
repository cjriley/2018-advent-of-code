import collections
import datetime
import re
import sys
from dataclasses import dataclass


@dataclass
class TimestampedRecord:
    timestamp: datetime.datetime
    message: str


def get_sorted_input():
    all_messages = []
    time_extracting_re = re.compile(
        r"\[(?P<DATE_STRING>\d{4}-\d{2}-\d{2} \d{2}:\d{2})] (?P<MESSAGE>.*)")
    for line in sys.stdin:
        match = time_extracting_re.match(line.strip())
        if not match:
            raise RuntimeError(f"Unexpected format: {line}")

        dt = datetime.datetime.strptime(match.group("DATE_STRING"), "%Y-%m-%d %H:%M")
        all_messages.append(
            TimestampedRecord(timestamp=dt, message=match.group("MESSAGE")))

    return sorted(all_messages, key=lambda m: m.timestamp)


sorted_input = get_sorted_input()

# Guard # > { minute # > count of that minute asleep }
guard_data = collections.defaultdict(lambda: collections.defaultdict(int))

guard_re = re.compile(r"Guard #(?P<NUMBER>\d+)")
current_guard = None
falls_asleep_minute = None

for item in sorted_input:
    guard_match = guard_re.search(item.message)
    if guard_match:
        current_guard = guard_match.group("NUMBER")
        continue
    elif "falls asleep" in item.message:
        falls_asleep_minute = item.timestamp.minute
    elif "wakes up" in item.message:
        for sleeping_minute in range(falls_asleep_minute, item.timestamp.minute):
            guard_data[current_guard][sleeping_minute] += 1


# Now find the sleepiest guard and his sleepiest minute
sleepiest_guard = None
sleepiest_minute_number = None
total_sleeping_time = 0
for guard_number, sleep_data in guard_data.items():
    total_minutes_asleep = sum(sleep_data.values())
    if total_minutes_asleep > total_sleeping_time:
        sleepiest_guard = guard_number
        total_sleeping_time = total_minutes_asleep
        sleepiest_minute_number, _ = max(sleep_data.items(), key=lambda x: x[1])

print(f"{int(sleepiest_guard) * sleepiest_minute_number}")
