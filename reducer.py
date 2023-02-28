#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

social_media_type = None
date = None
count = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split("\t")

    if len(tokens) != 3:
        print(tokens)
        continue

    current_social_media_type, current_date, _ = tokens

    if current_social_media_type == social_media_type and current_date == date:
        count += 1
    elif current_social_media_type == social_media_type and current_date != date:
        print(f"{social_media_type}\t{date}\t{count}")
        count = 1
        date = current_date
    else:
        if social_media_type:
            print(f"{social_media_type}\t{date}\t{count}")
        social_media_type = current_social_media_type
        date = current_date
        count = 1

print(f"{social_media_type}\t{date}\t{count}")
