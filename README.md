# ROS2 Talker and Listener 

## 概要
ROS2を使用したTalkerとlistenerのプロジェクトです。Talkerは"countup"トピックにInt16メッセージを定期的にパブリッシュし、データを1ずつ増やします。Listenerは"countup"というトピックからInt16メッセージを購読し、そのデータをログに表示します。

## Talker

### 使用方法
```python3
git clone https://github.com/ryutarou1/ros2 
cd 
cd ~/ros2_ws/src/mypkg/mypkg
ros2 talker.py
```
上記のコマンドを打つことによりTalkerのプロジェクトを使用することができます。

##  Listener

### 使用方法
Talkerのプロジェクトを使用した状態で、Talkerのプロジェクトとは違う新しいウィンドウを開きます。
```python3
cd 
cd ~/ros2_ws/src/mypkg/mypkg
ros2 listener.py
```
上記のコマンドを打つことによりListenerのプロジェクトを使用することができます。

### 動作例
```
$ ros2 listener.py
[INFO] [1703389372.824852203] [listener]: Listen: 84
[INFO] [1703389373.306178429] [listener]: Listen: 85
[INFO] [1703389373.805507318] [listener]: Listen: 86
[INFO] [1703389374.305980747] [listener]: Listen: 87
[INFO] [1703389374.805550151] [listener]: Listen: 88
```

## 実行環境
ros2

## テスト環境
Ubuntu 20.04.6 LTS (GNU/Linux 5.10.102.1-microsoft-standard-WSL2 x86_64)

## ライセンス
* このソフトウェアパッケージは三条項BSDライセンスのもと、再頒布および使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0by Ryuich Ueda)のものを、本人の許可を得て自身の著作したものです。r
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/
* This Softwere Package allowed Redistribution and Use by GPL 3.0
©2023 kanno ryutaro
