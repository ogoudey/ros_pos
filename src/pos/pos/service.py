from pos_interfaces.srv import AcceptCard, AddtoPurchase

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv1 = self.create_service(AcceptCard, 'accept_card', self.accept_card_callback)
        self.srv2 = self.create_service(AddtoPurchase, 'add_to_purchase', self.add_to_purchase_callback)
        self.customer = None
        self.card = None
        self.items = []
        
    def accept_card_callback(self, request, response):
        self.get_logger().info('Incoming request: ' + str(request.num) + ", " + request.name)
        self.customer = request.name
        self.card = request.num
        
        response.accept = True                                                  
        return response

    def add_to_purchase_callback(self, request, response):
        self.get_logger().info('Incoming request: ' + request.item)
        self.items += request.item

        
        response.success = True                                                  
        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
