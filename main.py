from datetime import date, timedelta

import urllib.request
import os
import re
from urllib.parse import urlparse


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def download_imgs(img_urls, dir_imgs):
    for i, url in enumerate(img_urls):
        try:
            # 4. URL からファイル名を取得
            # (例: https://i.imgur.com/ABCDEFG.jpg -> ABCDEFG.jpg)
            path = urlparse(url).path
            filename = os.path.basename(path)

            save_path = os.path.join(dir_imgs, filename)

            print("  ", url);

           #  # ユーザーエージェントを設定（サーバーからブロックされるのを避けるため）
           #  headers = {'User-Agent': 'Mozilla/5.0'}
           #  req = urllib.request.Request(url, headers=headers)

           #  with urllib.request.urlopen(req, timeout=10) as response:
           #      # 6. ファイルに保存
           #      with open(save_path, 'wb') as f:
           #          f.write(response.read())

        except urllib.error.HTTPError as e:
            # 404 Not Found や 500 Server Error など
            print(f" ! ダウンロード失敗: {url} (HTTPエラー: {e.code} {e.reason})")
        except urllib.error.URLError as e:
            # 接続エラーやタイムアウトなど
            print(f" ! ダウンロード失敗: {url} (URLエラー: {e.reason})")
        except Exception as e:
            print(f" ! 不明なエラー: {url} ({e})")


def main():
    dir_dirary = "/Users/tym/diary/"
    # /Users/tym/diary/2025/11/03.md
    # https://github.com/toasa/diary/blob/main/2023/02/03.md

    dir_imgs = "/Users/tym/tmp/backup-diary-images/imgs"

    # <img src="https://i.imgur.com/QJeJyTh.jpg" width="700">
    img_regex = re.compile(
        r'<img [^>]*src=["\'](https?://[^"\']+)["\'][^>]*>', re.IGNORECASE)

    d_start = date(2022, 8, 11)
    d_end = date.today()

    for d in daterange(d_start, d_end + timedelta(days=1)):
        diary_path = dir_dirary + d.strftime("%Y/%m/%d.md")
        if not os.path.exists(dir_dirary):
            continue
        
        # print(d.strftime("%Y/%m/%d.md"))

        with open(diary_path, 'r', encoding='utf-8') as f:
            content = f.read()

            image_urls = img_regex.findall(content)
            if not image_urls:
                continue

            download_imgs(image_urls, dir_imgs)


main()
