# Carrot ROS workspace
全自動走行台車のcatkin_wsです。
[Carrotの動画はこちら](https://www.youtube.com/watch?v=5gtot_12dCg&ab_channel=DDProjectII)


# Features

USBコントローラーで手動で動かしつつ、LiDARでSLAMをし環境マップを作成、作成したマップをもとに目的地まで自動走行をすることができます。

# Requirement
* Ubuntu 18.04
* ROS melodic

 -ROS package-
* cartographer
* cartographer_ros
* move_base
* joy
* lidar_utils

etc..

# Installation

catkin_ws/src以下にcloneし、catkin_makeをしてください。


# Usage

` roslaunch carrot usb_slam.launch` :usbコントローラーで動かしながらSLAMをします。その後map_saverで保存してください。

` roslaunch carrot move_base.launch` :/home/user/　直下のmap.pgmを読み込み自動走行します。

` roslaunch carrot_py usb-control.launch` :usbコントローラーでロボットを動かします。

# Note

モーター制御用のマイコンとシリアル通信をすることでロボットを動かしています。

モーター制御用マイコンのプログラムは[こちら](https://github.com/rakuseirobot/Carrot-F4-motor)

# Author

* Shun Kayaki
* Kyushu institute of Technology
* shun@guetan.dev

# License

Copyright (c) 2019 Shun Kayaki
Released under the MIT license
