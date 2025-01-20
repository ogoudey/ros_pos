from pos_interfaces.srv import AcceptCard

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AcceptCard, 'accept_card')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AcceptCard.Request()                                   # CHANGE

    def send_request(self, _input):
        num, name = _input.split(' ')
        self.get_logger().info('Sending (' + str(num) + ", " + name + ")")
        self.req.num = int(num)
        self.req.name = name
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init()
    while rclpy.ok():
        minimal_client = MinimalClientAsync()
        minimal_client.send_request(input("<num name>:"))


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
