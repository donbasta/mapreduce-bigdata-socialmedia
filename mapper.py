#!/home/farras/.pyenv/shims/python
"""mapper.py"""

import json
import sys

for line in sys.stdin:
    print(json.loads(line.strip()))
