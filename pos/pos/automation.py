import time
import random

import rclpy
from rclpy.node import Node

from pos_interfaces.msg import MockAction

class MinimalPublisher(Node):

    def __init__(self, plan_status, plan_of_actions):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(MockAction, 'action/mock', 10)
        
        counter = 0
        for action in plan_of_actions:
            plan_status = counter/len(self.plan)
            print("Imma do " + action)
            msg = MockAction()
            msg.action = action
            msg.time = counter
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.publisher_.publish(msg)
            time.sleep(1)
            counter += 1
        
class Actor:
    def __init__(self):
        self.plan = None


    def act(self, plan_status):
        if not self.plan:
            self.plan = self.generate_plan()

        return self.plan


        
            
            

    def generate_plan(self):
        # first make up what the hell is going on
        import yaml
        with open('/home/olin/Robotics/ros_pos_ws/src/price_lookup.yaml', "r") as file:
            items = list(yaml.safe_load(file).keys())
        default_plan = random.choices(items, k=100)
        # there are 100 items incoming and publishing actions called <item> is enough to scan the item
        return default_plan
