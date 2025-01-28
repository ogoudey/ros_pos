import rclpy
from rclpy.node import Node

from pos_interfaces.srv import Interaction

### Def. "interaction" is textual input... ###

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('interaction_client')
        self.cli = self.create_client(Interaction, 'interaction')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=3.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Interaction.Request()                                   # CHANGE

    def send_request(self, _input):
        text = _input
        self.get_logger().info('Sending: \"' + text + '\"')
        self.req.text = text
        return self.cli.call_async(self.req)

        
def main(args=None):
    rclpy.init()
    while rclpy.ok():
        minimal_client = MinimalClientAsync()
        future = minimal_client.send_request(input("<text>: "))

        rclpy.spin_until_future_complete(minimal_client, future)
        #rclpy.spin_once(minimal_client)
        response = future.result()
        
        minimal_client.get_logger().info("Response: " + response.response)
               
        minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
