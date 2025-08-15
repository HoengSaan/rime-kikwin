# 菊韻和語

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

本リポジトリは[コモンズ証 - 表示 - 非営利 - 継承 4.0 国際](cc-by-nc-sa)のもとで提供されます。

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

菊韻和語同其他主要基於mozc項目，使用音碼輸入日語之中州韻方案（Rime Scheme）有共同缺點，**難用**。此類方案打字體驗基本上只能滿足最基本日語打字需求，打字體驗甚至可能不如20年前ATOK、WX系列等輸入法（儘管此類輸入法並非無償）。

本人雖已有想法，但實際嘗試後，發現中州韻本身設計竝不利於日語輸入法，尤其是日語文法特徵。例如用言活用，中州韻需超巨大詞庫去，效率不符合實際使用。（電腦或許可以成功部署，但所需時間或遠超想像。或許lua亦能實現類似功能，但本人認爲最終結果不如直接使用原生日語輸入法。故菊韻和語或不再更新，亦不需要更新已可達成其元本功能，即使用菊韻時輔助性輸入日語。

This project will not receive any update, probably. For details, see the Chinese announcement above.

このプロジェクトはおそらく更新されません。詳細は上記の中国語でのお知らせをご覧ください。

## Introduction

**Kikwin** (菊韻, きくゐん) is a Japanese input method based on RIME. The major different between other Japanese scheme is the dictionary file use Kana instead of romaji, which significanlly lower the size of the file.

**Kikwin** is orginally intend as a tools to type Japanese while using **Gukwan** (菊韻), a Cantonese input method based on RIME, see [HoengSaan/rime-gukwan](https://github.com/HoengSaan/rime-gukwan/) for details.

**Kaomoji** is for typing kaomoji, press `K` to type kaomoji in **Kikwin**. The dictionary file is based on [mtripg6666tdr/Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj), which are subject to the license from which they are converted.

The following file is converted from [lazyfoxchan/rime-jaroomaji: Japanese rōmaji input schema for Rime IME](https://github.com/lazyfoxchan/rime-jaroomaji/), which are subject to the license from which they are converted. Please check the comment line of each dictionary file header for details.

- `kikwin.jmdict`
- `kikwin.kanjidic2`
- `kikwin.mozc`
- `kikwin.mozcemoji`

`kikwin.map` is based on Geospatial Information Authority of Japan's [地名集日本 (GAZETTEER OF JAPAN)](https://www.gsi.go.jp/kihonjohochousa/gazetteer.html)

Update: Added [rime-kunyomi](https://github.com/sgalal/rime-kunyomi/tree/master) dictionary, license unknown.

## はじめに

Kikwin（菊韻、きくゐん）は、RIMEに基づく日本語入力法です。

Kikwinはもともと、Gukwan（菊韻、広東語入力法）を使用しながら日本語を入力するツールとして作られました。詳しくは[HoengSaan/rime-gukwan](https://github.com/HoengSaan/rime-gukwan/) をご覧ください。

**Kaomoji**は顔文字を入力するためのもので、Kikwinで顔文字を入力する場合は`K`を押してください。辞書ファイルは[mtripg6666tdr/Kaomoji_proj](mtripg6666tdr/Kaomoji_proj)に基づいており、変換元のライセンスに従います。

以下のファイルは、[lazyfoxchan/rime-jaroomaji: Japanese rōmaji input schema for Rime IME](https://github.com/lazyfoxchan/rime-jaroomaji/) から変換されたものであり、変換元のライセンスに従います。各ファイルのコメントで詳細を確認してください。

- `kikwin.jmdict`
- `kikwin.kanjidic2`
- `kikwin.mozc`
- `kikwin.mozcemoji`

`kikwin.maps`の底本は国土地理院の[地名集日本 (GAZETTEER OF JAPAN)](https://www.gsi.go.jp/kihonjohochousa/gazetteer.html)。

アップデート：[rime-kunyomi](https://github.com/sgalal/rime-kunyomi/tree/master)辞書ファイル追加，ライセンス不明。

## 簡介

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入日文。

本方案本用作使用菊韻粵語方案時，免除切換日文輸入法麻煩而作。詳細：[HoengSaan/rime-gukwan](https://github.com/HoengSaan/rime-gukwan/) 。

以下文件從[lazyfoxchan/rime-jaroomaji: Japanese rōmaji input schema for Rime IME](https://github.com/lazyfoxchan/rime-jaroomaji/)自動轉換，遵守源文件之許可。詳細請見各文件備註。

- `kikwin.jmdict`
- `kikwin.kanjidic2`
- `kikwin.mozc`
- `kikwin.mozcemoji`

`kikwin.maps`底本爲國土地理院[地名集日本 (GAZETTEER OF JAPAN)](https://www.gsi.go.jp/kihonjohochousa/gazetteer.html)。

更新：增加[rime-kunyomi](https://github.com/sgalal/rime-kunyomi/tree/master)詞庫，許可證不明。
