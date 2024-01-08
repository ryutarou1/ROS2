#!/bin/bash
# SPDX-FileCopyrightText: 2023 kanno ryutaro
# SPDX-License-Identifier: GPL-3.0-or-later

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'process has finished cleanly'
