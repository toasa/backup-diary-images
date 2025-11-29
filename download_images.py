import urllib.request
import os
import sys
import json
import time
from urllib.parse import urlparse

BACKUP_DIR = "/Users/tym/tmp/backup-diary-images/imgs"

if len(sys.argv) != 2:
    print("Usage: {} IMAGE_LIST_JSON".format(sys.argv[0]))


with open(sys.argv[1], 'r', encoding='utf-8') as j:
    for day, urls in json.load(j).items():
        print(day)

        for url in urls:
           # ユーザーエージェントを設定（サーバーからブロックされるのを避けるため）
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)

            filename = os.path.basename(urlparse(url).path)
            save_path = os.path.join(BACKUP_DIR, filename)

            try:
                with urllib.request.urlopen(req, timeout=10) as resp,  open(save_path, 'wb') as f:
                    f.write(resp.read())
                    print("  Saved:", filename)

            except urllib.error.HTTPError as e:
                print(
                    f" Download failed!: {url} (HTTP error: {e.code} {e.reason})")
            except urllib.error.URLError as e:
                print(f" Download failed!: {url} (URL error: {e.reason})")
            except Exception as e:
                print(f" Unknown error: {url} ({e})")

            time.sleep(1)
