

1. YYYY/MM/DD をキー、日記内の画像ファイルのURLをバリューとする JSON を生成
2. JSON を参照して、画像をダウンロードする

---

\<img タグ：1507個
https://i.imgur：1503個

jpeg: 232個
jpg：1242個
png：37個

```
tym@:~/diary (main)$ grep -r "<img" 202* | grep -v "https://i.imgur"
2022/11/18.md:<img src="https://alu-web-herokuapp-com.global.ssl.fastly.net/cropped_images/UC5NhFjnTcPDG7Ke6dj8A1iZABK2/c_1586959074726?auto=webp&format=jpg&width=1360" width="500">
2022/10/07.md:<img src="https://pbs.twimg.com/media/E2LhDkDXoAILAi-?format=jpg&name=4096x4096" width="700">
2022/09/25.md:<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/A_Sunday_on_La_Grande_Jatte%2C_Georges_Seurat%2C_1884.jpg/2880px-A_Sunday_on_La_Grande_Jatte%2C_Georges_Seurat%2C_1884.jpg" width="700">
2023/01/13.md:<img src="https://www.ghibli.jp/gallery/marnie035.jpg" width="700">
```