#!/bin/bash
# SPDX-FileCopyrightText: 2023 kanno ryutaro
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# person_msgs パッケージ内の Query サービスのインターフェースをログに追加
ros2 interface show "person_msgs/srv/Query" >> /tmp/mypkg.log

timeout 10 ros2 launch mypkg talk_listen.launch.py >> /tmp/mypkg.log

# /tmp/mypkg.log ファイルから ': 21' を含む行だけを表示
cat /tmp/mypkg.log | grep ': 21'

