# Introduction2Brain Sample Programs
====

このレポジトリは全能アーキテクチャ・イニシアティブの「エンジニアのための脳科学入門」に出てくるアルゴリズムのサンプルを提供します。

提供するアルゴリズムは以下の通りです。

- SOM: Self Organizing Map
- CPG: Central Pattern Generator

TODO: Sparse Coding, Auto Encoder など

## Description

### SOM

SOM は１次視覚野（V1）で自己組織的に方位選択マップが生成されるものをモデル化したものです。多次元ベクトルを２次元上に整理整頓します。クラスタリング、次元削減などにも使用されます。

ここでは色とベクトルを SOM にかけるサンプルを提供します。

### CPG

動物には運動プリミティブと呼ばれる、生得的な運動機能があります。体の様々なところにある屈筋ニューロン、伸筋ニューロンが複雑な運動のパターンを生成しています。

数十の筋電位を計測し、データ解析をしたところ、４個の命令で数十の筋肉の活動を再現できることが発見されました。

ここではシンプルに二つの伸筋ニューロンと屈筋ニューロンで繰り返されるパターンを生成するサンプルを提供します。

パラメータを変化させるとパターンがどのように変化するか、確認してみてください。

## Requirement

Python 3、Swig といくつかの Python のライブラリが必要です。

## Install

pymvpa というライブラリを利用するために swig をインストールしてください。

> brew install swig

その後に requirements.txt で Python のライブラリをインストールしてください。

> pip install -r requirements.txt


## Usage

som 配下、neuro_oscillator_model 配下のファイルは python コマンドで実行してください。

プログラムの実行順序を追う場合は、デバッガで追うことも可能です。


## Contribution

参加したい場合は、[こちら](https://wba-initiative.org/join-sig-wba/)にお問合せください。

## Licence

+ Apache License, Version 2.0
+ Original Developer: ([DWANGO ARTIFICIAL INTELLIGENCE LABORATORY](http://ailab.dwango.co.jp/en/))

## Author

naoyuki.sakai[https://github.com/naoyuki-sakai]
