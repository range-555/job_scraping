
# Qiita URL
<a href="https://qiita.com/range_555/items/acd94def2240d7060ec0
" rel="nofollow noopener">Pythonでwebエンジニアになるために必要なスキルを探ってみた</a>

# 概要
上記の記事にて、転職サイトから情報をスクレイピングする際に使用したコードです。

# 各ファイルの説明

- `getJobsearchPageurl.py`
検索ワードを入力した結果ページから各求人のurlを取得し、DBに格納

- `getJobsearchHTML.py`
各求人urlからhtmlを取得し、DBに格納

- `getJobsearchContents.py`
DBに格納した各求人のhtmlから求人に関するデータを取得し、DBに格納

- `analysisJobSearch.ipynb`
求人データから、必要スキルとして挙げられた頻度の高い単語を分析

- `requirements.txt`
今回の分析で使用したパッケージ設定