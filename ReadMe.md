# Simple Translater for Excel To Japanese

## Requirements

Install the necessary package if you don't have
```
pip install -r requirements.txt
```
## Usage

Translate Colnum A in excel file, and save as an another file.

Put your target file same as translate.py

Usage: python translate [dest lang] [input file] [output file]
Args(default):
- dest language: ja
- input file name: in.xlsx
- output file name: out.xls

## 日本語

エクセルのA列にいる文字を翻訳し、別のファイルに出力

翻訳したいファイルをtranslate.pyと同じフォルダに置いてください。
実行方法： python translate [dest lang] [input file] [output file]
引数（デフォルト値）
- どの言語に翻訳: ja
- 対象ファイル: in.xlsx
- 出力ファイル: out.xls

---

Test under python version 3.8