#!/home/farras/.pyenv/shims/python
"""reducer.py"""

import sys

social_media_type = None
date = None
count = 0

with open("output", "w+") as w:
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
            w.write(f"{social_media_type}\t{date}\t{count}\n")
            # print(f"{social_media_type}\t{date}\t{count}")
            count = 1
            date = current_date
        else:
            if social_media_type:
                w.write(f"{social_media_type}\t{date}\t{count}\n")
                # print(f"{social_media_type}\t{date}\t{count}")
            social_media_type = current_social_media_type
            date = current_date
            count = 1

    w.write(f"{social_media_type}\t{date}\t{count}\n")
    # print(f"{social_media_type}\t{date}\t{count}")
