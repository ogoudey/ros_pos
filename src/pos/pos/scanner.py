from pos_interfaces.srv import AddtoPurchase

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddtoPurchase, 'add_to_purchase')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddtoPurchase.Request()                                   # CHANGE

    def send_request(self, _input):
        item = _input
        self.get_logger().info('Sending (' + str(item) + ")")
        self.req.item = item
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init()
    while rclpy.ok():
        minimal_client = MinimalClientAsync()
        minimal_client.send_request(input("<item>:"))


        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info('Response!')  # CHANGE
            

        minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
