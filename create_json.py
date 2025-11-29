from datetime import date, timedelta

import os
import re
import json


# {
#   "YYYY/MM/DD.md": [
#     "画像URL_1",
#     "画像URL_2",
#     "..."
#   ],
#   "2025/11/27.md": [
#     "https://example.com/images/20251127_sunset.jpg",
#     "https://example.com/images/20251127_coffee.png"
#   ],
#   "2025/11/28.md": [
#     "https://example.com/images/20251128_meeting_diagram.gif"
#   ],
#   "2025/11/29.md": [],
#   "...": "..."
# }


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


dir_dirary = "/Users/tym/diary/"

# <img src="https://i.imgur.com/QJeJyTh.jpg" width="700">
img_regex = re.compile(
    r'<img [^>]*src=["\'](https?://[^"\']+)["\'][^>]*>', re.IGNORECASE)

d_start = date(2022, 8, 11)
d_end = date.today()

imgs_map = {}

for d in daterange(d_start, d_end + timedelta(days=1)):
    diary_filename = d.strftime("%Y/%m/%d.md")
    diary_path = dir_dirary + diary_filename
    if not os.path.exists(diary_path):
        continue

    with open(diary_path, 'r', encoding='utf-8') as f:
        content = f.read()

        img_urls = img_regex.findall(content)
        if not img_urls:
            continue

        imgs_map[diary_filename] = img_urls

print(json.dumps(imgs_map, indent=4))
