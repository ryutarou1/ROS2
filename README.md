# ROS2 Talker.py and Listener.py 

## 概要
ROS2を使用したTalker.pyとlistener.pyのプロジェクトです。Talker.pyは"/countup"トピックにInt16メッセージを定期的にパブリッシュし、データを1ずつ増やします。Listener.pyは"/countup"というトピックからInt16メッセージを購読し、そのデータをログに表示します。

## Talker.py

### 実行方法
```ros2 
$ ros2 run mypkg talker.py
```
* 上記のコマンドを打つことによりTalker.pyのプロジェクトを使用することができます。
* 上記のTalker.pyのプロジェクトを実行しても何も表示されません。

##  Listener.py

### 実行方法
Talker.pyのプロジェクトを使用した状態で、Talker.pyのプロジェクトとは違う新しいウィンドウを開きます。
```ros2
$ ros2 run mypkg listener.py
```
上記のコマンドを打つことによりListener.pyのプロジェクトを使用することができます。

### 動作例
```
$ ros2 run mypkg listener

[INFO] [1703899748.083843531] [listener]: Listen: 12
[INFO] [1703899748.446453092] [listener]: Listen: 13
[INFO] [1703899748.946614171] [listener]: Listen: 14
[INFO] [1703899749.446456161] [listener]: Listen: 15
[INFO] [1703899749.946887823] [listener]: Listen: 16
[INFO] [1703899750.446357793] [listener]: Listen: 17
[INFO] [1703899750.946671646] [listener]: Listen: 18
```

## Talk_listen.lunch.py

### 実行方法
```ros2
$  ros2 launch mypkg talk_listen.launch.py
```
上記のコマンドを入力することでlunchファイルを使用することができる。

### 動作例
```
[INFO] [launch]: All log files can be found below /home/...
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [4689]
[INFO] [listener-2]: process started with pid [4691]
[listener-2] [INFO] [1703900472.848043051] [listener]: Listen: 0
[listener-2] [INFO] [1703900473.321967055] [listener]: Listen: 1
[listener-2] [INFO] [1703900473.822310169] [listener]: Listen: 2
[listener-2] [INFO] [1703900474.322066593] [listener]: Listen: 3
[listener-2] [INFO] [1703900474.821856995] [listener]: Listen: 4
[listener-2] [INFO] [1703900475.321884910] [listener]: Listen: 5
```
launchファイルを使用することで、talker.pyとlistener.pyの実行を同時に行うことができる.

## テスト環境
* Ubuntu 22.04
* Python
* Ros 2 humble

## 著作権およびライセンスについて
* このソフトウェアパッケージは三条項BSDライセンスのもと、再頒布および使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0by Ryuich Ueda)のものを、本人の許可を得て自身の著作したものです。
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson7.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/
https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/
* ©2023 kanno ryutaro
