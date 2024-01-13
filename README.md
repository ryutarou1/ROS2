# ROS2 Talker and Listener 

## 概要
このプログラムはROS 2で書かれたもので、サービス通信を使用して、質問に応答するtalkerというノードと、その質問を行うlistenerというノードを実装しています。

## Query サービス

`query` サービスは、名前に基づいて人物の年齢情報を取得するために使用されます。

### メッセージの構造

このサービスは `person_msgs/Query` メッセージを使用しており、`name` フィールドで人物の名前を指定し、`age` フィールドで年齢情報を受け取ります。

## Talker

### 使用方法
```ros2
git clone https://github.com/ryutarou1/ros2 
cd ros2_ws
ros2 run mypkg talker.py
```
上記のコマンドを打つことによりTalkerのプロジェクトを使用することができます。

##  Listener

### 使用方法
Talkerのプロジェクトを使用した状態で、Talkerのプロジェクトとは違う新しいウィンドウを開きます。
```ros2
cd ros2_ws
ros2 run mypkg listener.py
```
上記のコマンドを打つことによりListenerのプロジェクトを使用することができます。

## 実行結果
"ryu"という名前での呼び出しではage: 21、それ以外の場合はage: 255が表示されます。

## 実行環境
ros2

## テスト環境
* Ubuntu 20.04.6 LTS (GNU/Linux 5.10.102.1-microsoft-standard-WSL2 x86_64)
* Ubuntu 22.04

## ライセンス
* このソフトウェアパッケージは三条項BSDライセンスのもと、再頒布および使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0by Ryuich Ueda)のものを、本人の許可を得て自身の著作したものです。
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/
* This Softwere Package allowed Redistribution and Use by BSD 3.0
©2023 kanno ryutaro
