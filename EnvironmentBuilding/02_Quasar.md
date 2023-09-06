# Quasarとは
QuasarとはVue.jsをベースにしたWebフレームワークの1つです．この地上局にはfrontendとして使用しました．<br>
[公式HP](https://quasar.dev/)

# Quasarの環境構築
Quasarのインストール方法を以下の記事を参考に進めていきます．<br><br>
[Quasar frameworkの始め方(Vueフレームワーク)](https://devsakaso.com/vue-js-quasar-start/)

## Node.jsの準備
まずはNode.jaがインストールされているかを確認します．以下のコマンドを実行して確認してください．

```bash
node -v
```

バージョンが表示されなかったらnode.jsをインストールする必要あります．バージョンが表示されたらインストール完了しています．完了している場合は次の章を飛ばしていただいても構いませんが，最新のバージョンにしておくことをおすすめします．

## Node.jsをインストール
[公式HP](https://nodejs.org/ja)から最新安定版をインストールしてください．ダウンロード後は指示に従って進めてください．

すべての設定が終わったら再起動する必要があります．その後もう一度上記のやり方でバージョンを確認してください．

```bash
node -v
```
バージョンを確認出来たらインストール完了です．

## Quasar CLIをインストールする

Quasarをインストールする方法は3通りあります．特別な理由がない限り，Quasar ClIを使うことをおすすめします．違いを知りたい方は[公式HP](https://quasar.dev/)を参照してください．

以下のコマンドを実行してください．
```bash
yarn global add @quasar/cli
#or
npm install -g @quasar/cli
```

以下のような結果が出たらインストール完了です．
```bash
___
/ _ \ _ _ __ _ ___ __ _ _ __
| | | | | | |/ _` / __|/ _` | '__|
| |_| | |_| | (_| \__ \ (_| | |
\__\_\\__,_|\__,_|___/\__,_|_|
```

# Quasarの実行方法
frontend階層にします．

```bash
cd Misson3-SERVER-sample
cd cd frontend
```

次に以下のコマンドを実行します．

```bash
npm run dev
```
以下のようなサーバが立ち上がったら成功です．<br><br>
![overview_HP](/images/overview_HP.png)
