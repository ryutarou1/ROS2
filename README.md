# mypkg

## 概要
このプOSディストリビューションログラムはROS 2で書かれたもので、サービス通信を使用して、質問に応答するtalker.pyというノードと、その質問を行うlistener.pyというノードを実装しています。

## Query サービス

`query` サービスは、名前に基づいて人物の年齢情報を取得するために使用されます。

### メッセージの構造

このサービスは `person_msgs/Query` メッセージを使用しており、`name` フィールドで人物の名前を指定し、`age` フィールドで年齢情報を受け取ります。

## talker.py

### 実行方法
```ros2
ros2 run mypkg talker.py
```
上記のコマンドを打つことによりTalker.pyのプロジェクトを使用することができます。

##  Listener.py

### 使用方法
Talker.pyのプロジェクトを使用した状態で、Talker.pyのプロジェクトとは違う新しいウィンドウを開きます。
```ros2
ros2 run mypkg listener.py
```
上記のコマンドを打つことによりListener.pyのプロジェクトを使用することができます。

## 実行結果
"ryu"という名前での呼び出しではage: 21、それ以外の場合はage: 255が表示されます。

## テスト環境
* Ubuntu 20.04.6 LTS (GNU/Linux 5.10.102.1-microsoft-standard-WSL2 x86_64)
* Ubuntu 22.04

## 著作権およびライセンスについて
* このソフトウェアパッケージは三条項BSDライセンスのもと、再頒布および使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0by Ryuich Ueda)のものを、本人の許可を得て自身の著作したものです。
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/
* ©2023 kanno ryutaro
