#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("cool_node")
        num = 1
        self.get_logger().info(f"My log message {num}")


def main(args=None):
    rclpy.init(args=args)
    
    aNode = MyNode()
    rclpy.spin(aNode)

    rclpy.shutdown()


if __name__ == '__main__':
    main(   )