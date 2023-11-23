# Djangoとは
DjangoとはPythonで書かれたWebフレームワークの1つです．この地上局ではbackendとして使用しています．<br>
[公式HP](https://docs.djangoproject.com/ja/4.2/)

# 環境構築
Djangoの環境構築は以下の記事を参考に進めます．<br>
[Ubuntu 20.04にDjangoをインストールする方法](https://tutorialcrawler.com/ubuntu-debian/ubuntu-20-04%E3%81%ABdjango%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)

## Pythonのインストール
UbuntuにはデフォルトでPythonが入っていますが，念のため確認しておきます．

```bash
python3 --version
```
バージョンが返ってきたらインストール済みで，返ってこなかったらインストールする必要があります．

## Djangoのインストール
Djangoをインストールするために以下のコマンドを実行してください．

``` bash
pip3 install Django
```
インストーrが終わったら以下のコマンドを実行してください

``` bash
django-admin --version
```

バージョンが返ってきたらインストール成功です．

# 最後に
Djangoは公式のチュートリアルが豊富です．ぜひ，参考にしてみてください．
[はじめての Django アプリ作成、その 1](https://docs.djangoproject.com/ja/4.2/intro/tutorial01/)
