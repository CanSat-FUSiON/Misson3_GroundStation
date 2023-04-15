# MISSON3の地上局

サーバーを立ち上げて機体に搭載されているカメラからストリームを確認したり機体を制御したり出来ます．

# 作業環境

Visual Studio Code

# 環境構築

## Ubuntuの導入

### Windows Subsystem for Linux(WSL)の有効化

1. Windowsの検索窓にPowerShellと入力しPowerShellを管理者として実行する
2. WSLが既に入っているか確認する
```console
wsl
```
何もエラーが出なかったらインストールは完了している.
インストールが完了している場合は飛ばしてもよい
3. PowerShell上で下記を実行する
```console
wsl --install
```
Windowsのバージョンが古い場合はこのコマンドが対応していない可能性があるので，その場合は[コチラ](https://learn.microsoft.com/ja-jp/windows/wsl/install)を参照してください

### 仮想マシンの有効化

1. 検索窓からコントロールパネルを開く
2. 「Windowsの機能の有効化または無効化」をクリック
3. 「仮想マシン　プラットフォーム」という項目のチェックボックスをオンにする

### Linux更新プログラムのダウンロード・インストール

1. [コチラ](https://www.google.com/url?q=https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi&sa=D&source=docs&ust=1681273590548343&usg=AOvVaw3lGgwCjxQPWaUCsQ6sGupu)をクリック
2. ダウンロードが完了したらプログラム実行してインストールする．エラーが発生した場合はWindowsの更新をしたうえでもう一度実行して見てください

### WSLの有効化

先ほど出てきた「Windowsの機能の有効化と無効化」の中にある「Linux用Windowsのサブシステム」のチェックボックスをオンにする

### WSLのバージョンを選択

PowerShellを立ち上げて次のコマンドを実行する
```console
wsl -set-default-version2
```

### Ubuntuのインストール

1. Microsoft StoreからUbuntuをインストールする．バージョンは基本的にどれでもよい
2. インストールが完了したら初期設定を済ませる．パスワードは忘れないで

## Visual Studio Codeのインストール

1. [コチラ](https://code.visualstudio.com/)からVisual Studio Codeをインストールする
2. インストールが完了したら左にあるタブの下のExtensionをクリックして検索窓に「remote wsl」と入力しインストールする
3. 「remote wsl」のインストールが完了したら1度閉じて再起動する
4. 左下にあるオレンジ色or緑色のアイコンをクリックする
5. 「New WSL Window using Disro...」をクリックしてインストールしたUbuntuを選択する
6. 左下の表示がWSL:Ubuntuになっていることを確認する

## WSLとgitの設定

1. gitをWSLにインストール　
```console
sudo apt install git
```
2. 設定
ユーザー名とメールアドレスを登録
```console
git config –global user.name “XXXXX”
git config –global user.email XXXXX@XXXXX
```
設定できていることを確認する(コマンドを入力して設定した値が返ってきたらOK)
```console
git config user.name
git config user.email
```

## githubの中にある既存のリポジトリーをクローンする

1. [コチラ](https://github.com/CanSat-FUSiON/MISSON3-SERVER-sample)の中にある緑色のCodeをクリックし，SSHをコピーする．
2. Windowsの検索窓からターミナルを開きUbuntuを開く
3. クローンする
```console
git clone https://github.com/CanSat-FUSiON/MISSON3-SERVER-sample
```

# 実行方法
サーバーを立ち上げるには，このコマンドを実行する
```console
cd MISSON3-SERVER-sample
cd frontend
npm run dev
```


