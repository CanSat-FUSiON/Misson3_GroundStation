# WindowsでLinux環境を構築する

Windows Subsystem for Linux(WSL)を使用してLinux環境を構築していきます．

本記事はWindowsを想定しています．Mac OSはLinuxと似ていることから，Linux環境を構築する構築する必要はありません．Macを使用している方は本記事を読み飛ばしていただいても構いません．

## WSLのインストール
まず，Windowsの検索窓に「Power Shell」と入力し，Powe Shellを立ち上げます．この際，管理者として実行する必要があります．<br><br>
![PowerShellWin.png](/images/PowerShellWin.png)
*PoweShellの立ち上げ画面*<br><br>


以下のコマンドを打ってWSLをインストールします．
```bash
wsl --install
```

## 仮想マシンの有効化
仮想マシンとは「あるコンピュータの中に違うコンピュータをインストールすることが出来る仕組み」というイメージです．詳しくは[こちら](https://hnavi.co.jp/knowledge/blog/virtual-machine/)をご覧ください．

1. Windowsの検索窓に「コントロールパネル」を表示させます
2. 「プログラム」をクリックします
3. 「Windowsの機能の有効化または無効化」をクリックします
4. 「仮想マシン　プラットフォーム」という項目のチェックボックスをオンにします

これで仮想マシンが有効になりました．

## WSLの有効化
仮想マシンの有効化と同様，「Windowsの機能の有効化または無効化」の中にある「Linux用Windowsサブシステム」のチェックボックスをオンにするとWSLが有効になります．

## WSLのバージョンの選択
特別な理由がない限り，WSLのバージョンは2を選ぶことをおすすめします．
PowerShellで以下のコマンドを実行してください．

```bash
wsl --set-default-version 2
```

これでバージョン２のWSLを有効化することが出来ました．

## Ubuntuのインストール
Microsoft StoreからUbuntuと検索します．ダウンロードするバージョンは基本的にどれでもよいです．<br>
インストールが終わったら一度立ち上げユーザー名とパスワードを入力します．パスワードは今後，使用するので**絶対に忘れないでください**．

## Visual Studio Codeのインストール
Visual Studio Codeとは言わずと知れた統合開発環境です．[こちら](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)からインストールしてください．<br>

次にVisual Studio Code上でUbuntuを操作するためのツールを導入します．まずVisual Studio Codeを立ち上げ，左にあるタブのExtensionをクリックします．その検索窓に「remote wsl」と入力しインストールします．インストールが終わったら終わったらVisual Studio Codeを再起動させます．<br>

その後，左下にあるオレンジor緑色のアイコンをクリックします．クリックすると画面中央に「New WSL Window using Disro...」と表示されるのでインストールしたUbuntuをクリックします．<br>

これでVisual Studio CodeのインストールとVisual Studio Code上でUbuntuを操作出来るようになっています．

## GitHubとVisual Studio Codeの接続方法
GitHubとVisual Studio Codeの接続方法は[こちら](https://github.com/CanSat-FUSiON/CanSat_Fundamentals/blob/main/teach_04_EnvironmentBuilding/01_Git_and_VisualStudioCode.md#zapgithub%E3%81%A8visualstudiocode%E3%81%AE%E6%8E%A5%E7%B6%9A%E6%96%B9%E6%B3%95)を参照してください．

# 環境構築
このリポジトリをクローンします．
```bash
cd /path/to/your/directory
git clone git@github.com:CanSat-FUSiON/MISSON3-SERVER-sample.git
cd MISSON3-SERVER-sample
```
これでローカル環境を構築することが出来ました．
