# SPDX-FileCopyrightText: 2023 kanno ryutaro
# SPDX-License-Identifier: GPL-3.0-or-later

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "ryu"
    future = client.call_async(req)
