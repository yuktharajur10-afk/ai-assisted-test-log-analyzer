import re
import pandas as pd

def parse_logs(file_path):
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
    rows = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                date, time, level, message = match.groups()
                rows.append({
                    "date": date,
                    "time": time,
                    "level": level,
                    "message": message
                })

    return pd.DataFrame(rows)
