from pos_interfaces.srv import AcceptCard, AddtoPurchase

import rclpy
from rclpy.node import Node

from pos import gui
from pos import connector as c
# from pos import llmi


import threading


def start_gui(state):
    gooey = gui.GUI(state)
    
class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv1 = self.create_service(AcceptCard, 'accept_card', self.accept_card_callback)
        self.srv2 = self.create_service(AddtoPurchase, 'add_to_purchase', self.add_to_purchase_callback)
        self.customer = None
        self.card = None
        
        ### STATE (ALSO MODIFIED BY GUI) ###
        self.state = {
            "ringing up": True,
            "items": [],
            "prices": [],
            "card": None,
        }
        


        s = threading.Thread(target=start_gui, args=[self.state])
        s.start()
        print("GUI started from service node.")
        
        # DATABASE
        self.db = c.Database() #Already exists
        self.db.drop_table()
        self.db.create_price_lookup_table()
        self.db.insert_data()
        
      
         
    def accept_card_callback(self, request, response):
        self.get_logger().info('Incoming request: ' + str(request.num) + ", " + request.name)
        self.customer = request.name
        
        self.state["card"] = request.num
        response.accept = True                                                  
        return response

    def add_to_purchase_callback(self, request, response):
        self.get_logger().info('Incoming request: ' + request.item)
        if self.state["ringing up"]:
            self.get_logger().info('Adding request to items: ' + request.item)
            self.state["items"].append(request.item)
            self.state["prices"].append(self.db.lookup_price(request.item))
        else:
            self.get_logger().info('Ignoring request:' + request.item)
        
        response.success = True                                                  
        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
