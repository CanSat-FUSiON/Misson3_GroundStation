# Misson3の地上局

このリポジトリーはMisson3が使用した地上局である．

# 概要
遠隔地で，ラジコン操作が可能なアプリケーションのサーバーを立ち上げる．この時，ngrokを使用しローカルのネットワークを外部に公開する．通信概略図を以下に示す．<br><br>

![overview.png](/images/overview.png)<br><br>

機体のESP-WROOM-32・ESP32-CAMでは，Wi-Fiの接続と同時にwebserverが立ち上がるようプログラミングし，ngrokを用いて外部から通信できるようにする，<br><br>

![overvier_HP](/images/overview_HP.png)<br><br>

HPには，「right」，「left」，「forward」，「back」，「fire」等のボタンを用意し，それぞれバックエンドサーバへリクエストを送信できるようにする．backendでは，受けたリクエストに応じて，ESP-WROOM-32にそれぞれ別のリクエストを送信し，右旋回，左遷会，前進，後退，ニクロム線を切るといった制御を行う．制御する人はESP32-CAMからのStreamを確認しながらゴールを目指す．<br>

上記に記載された内容は種子島ロケットコンテスト2023の遠隔制御部門にて使用した．同コンテストのミッション部門では自律走行していた機体のセンサが一部，故障するというミッションであった．そのために「EERGENC STOP」のボタンを用意し，その後は遠隔で機体を制御できるようになっている．

# 方法
まずESP-WROOM-32とESP32-CAMのサーバーを立ち上げる．その後，ngrokを用いてトンネリングし外部へ公開することで，遠隔地からの制御が可能となる．<br>
ngrokの使用方法や複数のポートをトンネリングする方法は以下のサイトを参照してください．<br><br>
[ngrokをインストールする方法を簡単な使い方](https://www.mgo-tec.com/blog-entry-ngrok-install.html)<br>
[ngrokを使用して複数ポートをhttps化する](https://qiita.com/MS-0610/items/8334bd1c165ea63ae566)

