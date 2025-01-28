from pos_interfaces.srv import AddtoPurchase

from pos_interfaces.msg import MockAction

import rclpy
from rclpy.node import Node

import threading

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddtoPurchase, 'add_to_purchase')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=3.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddtoPurchase.Request()                                   # CHANGE
        self.get_logger().info('Adding to purchase ready.')
    def send_request(self, item):

        self.get_logger().info('Sending ' + str(item))
        self.req.item = item
        self.future = self.cli.call_async(self.req)

class MinimalSubscriber(Node):

    def __init__(self, scan_event, scanned_items):
        super().__init__('minimal_subscriber')
        self.scan_event = scan_event
        self.scanned_items = scanned_items
        self.subscription = self.create_subscription(
            MockAction,
            'action/mock',
            self.callback,
            10)
        self.get_logger().info('Mock action scanner ready.')


    def callback(self, msg):
        self.get_logger().info('Action: ' + str(msg.action) + ' Time: ' + str(msg.time))
        
        self.scanned_items[0] = msg.action
        self.scan_event.set()
        


def scanner(scan_event, scanned_items):
    
    minimal_subscriber = MinimalSubscriber(scan_event, scanned_items)

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()

    

def main(args=None):
    rclpy.init()
    
    scan_event = threading.Event()
    scanned_items = [None] # this is a list so that passing it to the subscriber passes a deep copy
    scanner_ = threading.Thread(target=scanner, args=[scan_event, scanned_items])
    scanner_.start()
    
    while rclpy.ok():
    
 
    
        minimal_client = MinimalClientAsync()
        #minimal_client.send_request(input("<item>:"))
        
        scan_event.wait()
        minimal_client.send_request(scanned_items[0])

        #rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info('Response!')  # CHANGE
            
        scan_event.clear()
        minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
