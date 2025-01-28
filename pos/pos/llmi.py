from pos_interfaces.srv import Interaction
from pos_interfaces.msg import MockAction

import rclpy
from rclpy.node import Node

from pos import llm as l
from pos import automation

import threading
import time


class LLMI(Node):
    def __init__(self, pos_state=None):
        super().__init__('interaction_service')
        self.srv = self.create_service(Interaction, 'interaction', self.interact)
        self.pos_state = pos_state
        
        self.llm = l.LLM()
        
        self.publisher_ = self.create_publisher(MockAction, 'action/mock', 10)
        
        actor = automation.Actor()
        self.plan_status = 0
        self.plan_index = 0
        self.plan_of_actions = actor.act(self.plan_status)
        
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
            
    def timer_callback(self): # trigger mock actions
        if self.plan_index >= len(self.plan_of_actions) - 1:
            self.plan_index = 0
            self.get_logger().info('Starting over...')
        self.plan_status = self.plan_index/len(self.plan_of_actions)
        msg = MockAction()
        msg.action = self.plan_of_actions[self.plan_index]
        msg.time = self.plan_index
        self.plan_index += 1
        self.get_logger().info('Publishing, action: ' + msg.action + " Time: " + str(msg.time))
        self.publisher_.publish(msg)
        
    def interact(self, request, response):
        self.get_logger().info('Incoming request: ' + str(request))
        text = request.text
        llm_response = self.llm.textual_completion(str(self.plan_status) + "\n", text)
        
        response.response = llm_response                                                  
        return response
        
    def done_scanning(self):
        gui.button.invoke()


def main(args=None):
    
    
    rclpy.init(args=args)

    interaction_service = LLMI()
    
    rclpy.spin(interaction_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
